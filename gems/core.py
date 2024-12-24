import pathlib
from typing import *

from gems import base
from gems.facets import gems_query, local_ids_update, local_tags_update, attrs_update, global_ids_update, \
    global_tags_update, attrs_query, local_ids_query, global_tags_query, gems_update
from pdml import loader, saver


def create_gem(cluster: base.Cluster, gem_parent: base.Gem, gem_base_name: str) -> base.Gem:
    gem = base.Gem()
    attrs_update.set_cluster(gem, cluster)
    gems_update.add_child_gem(gem_parent, gem)
    attrs_update.set_gem_parent(gem, gem_parent)
    local_ids_update.set_gem_base_name(gem, gem_base_name)
    return gem


def make_gem(cluster: base.Cluster, gem_parent: base.Gem, gem_base_name: str) -> base.Gem:
    gem = local_ids_query.get_gem_by_gem_base_name(cluster, gem_base_name)
    if gem:
        return gem
    return create_gem(cluster, gem_parent, gem_base_name)


def mapped_gem_class(gem: Optional[base.Gem]) -> Optional[type]:
    class_name = attrs_query.get_class_name(gem)
    if class_name is None:
        return
    return base.class_map[class_name]


def reclass_facets(refined: dict, fname: str, facet: any) -> None:
    match fname:
        case "GemsFacet":
            refined_facet = base.GemsFacet()
            refined[fname] = refined_facet
            for child in facet:
                refined_facet.append(reclass(child, base.Gem))
        case "AttrsFacet":
            refined_facet = base.AttrsFacet()
            refined_facet.update(facet)
            refined[fname] = refined_facet
        case "GlobalIdsFacet":
            refined_facet = base.GlobalIdsFacet()
            refined_facet.update(facet)
            refined[fname] = refined_facet
        case "LocalIdsFacet":
            refined_facet = base.LocalIdsFacet()
            refined_facet.update(facet)
            refined[fname] = refined_facet
        case "GlobalTagsFacet":
            refined_facet = base.GlobalTagsFacet()
            refined_facet.update(facet)
            refined[fname] = refined_facet
        case _:
            refined[fname] = facet


def reclass(raw: dict, cls: type) -> base.Gem:
    refined = cls()
    for fname, facet in raw.items():
        reclass_facets(refined, fname, facet)
    subclass = mapped_gem_class(refined)
    if subclass:
        refined.__class__ = subclass
    return refined



def register(raw_cluster: dict, cluster_name: str, cluster_path: str) -> base.Cluster:
    cluster = reclass(raw_cluster, base.Cluster)
    assert isinstance(cluster, base.Cluster)
    global_ids_update.set_cluster_name(cluster, cluster_name)
    attrs_update.set_cluster_path(cluster, cluster_path)
    for gem, gem_parent in gems_query.get_gems(cluster, None):
        if gem_parent:
            attrs_update.set_gem_parent(gem, gem_parent)
            attrs_update.set_cluster(gem, cluster)
        local_ids_update.build_index(gem)
        local_tags_update.build_index(gem)
        global_ids_update.build_index(gem)
        global_tags_update.build_index(gem)
    return cluster


def load(cluster_path: pathlib.Path) -> base.Cluster:
    cluster_file_name = cluster_path.name
    cluster_name = cluster_file_name.split(".")[0]
    raw_cluster = loader.file_reader(cluster_path)
    cluster = register(raw_cluster, cluster_name, str(cluster_path))
    return cluster


def save(cluster: base.Cluster) -> None:
    cluster_path = attrs_query.get_attr_value(cluster, "#cluster_path")
    saver.writer(cluster_path, cluster)


def save_as(cluster: base.Cluster, cluster_path) -> None:
    saver.writer(cluster_path, cluster)


def unplug(cluster: base.Cluster) -> None:
    for gem, _ in gems_query.get_gems(cluster, None):
        global_ids_update.deindex(gem)
        global_tags_update.deindex(gem)


def build_aggregate() -> None:
    aggregate: base.Aggregate = base.Aggregate()
    base.set_aggregate(aggregate)


def create_resource_gem(resource_name: str, function: Callable) -> dict:
    aggregate = base.get_aggregate()
    resources = make_gem(aggregate, aggregate, "Resources")
    group = resource_name.split(".")[0]
    resource_group_gem = make_gem(aggregate, resources, group)
    resource_gem = create_gem(aggregate, resource_group_gem, resource_name)
    attrs_update.set_function(resource_gem, function)
    return resource_gem


def get_resource_gem(resource_name: str) -> Optional[base.Gem]:
    aggregate = base.get_aggregate()
    resource_gem = local_ids_query.get_gem_by_gem_base_name(aggregate, resource_name)
    return resource_gem


def get_resource_description(resource_name: str) -> Optional[base.dict_keys]:
    resource_gem = get_resource_gem(resource_name)
    if resource_gem is None:
        return None
    descriptions = global_tags_query.get_descriptions(resource_gem)
    return descriptions


def get_resource_function(resource_name: str) -> Optional[Callable]:
    resource_gem = get_resource_gem(resource_name)
    if resource_gem is None:
        return None
    function = attrs_query.get_function(resource_gem)
    return function


def initialize(home_path: pathlib.Path) -> None:
    build_aggregate()
