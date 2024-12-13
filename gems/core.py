import pathlib
import typing

from gems import base
from gems.facets import gems_query, local_ids_update, local_tags_update, attrs_update, global_ids_update, \
    global_tags_update, attrs_query, local_ids_query, global_tags_query, gems_update, global_ids_query
from pdml import loader, saver


def create_gem(cluster: dict, gem_parent: dict, gem_base_name: str) -> dict:
    gem = {}
    attrs_update.set_cluster(gem, cluster)
    gems_update.add_child_gem(gem_parent, gem)
    attrs_update.set_gem_parent(gem, gem_parent)
    local_ids_update.set_gem_base_name(gem, gem_base_name)
    return gem


def make_gem(cluster: dict, gem_parent: dict, gem_base_name: str) -> dict:
    gem = local_ids_query.get_gem_by_gem_base_name(cluster, gem_base_name)
    if gem:
        return gem
    return create_gem(cluster, gem_parent, gem_base_name)


def register(cluster: dict, cluster_name: str, cluster_path: str) -> None:
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


def load(cluster_path: pathlib.Path) -> dict:
    cluster_file_name = cluster_path.name
    cluster_name = cluster_file_name.split(".")[0]
    cluster = loader.file_reader(cluster_path)
    register(cluster, cluster_name, str(cluster_path))
    return cluster


def save(cluster: dict) -> None:
    cluster_path = attrs_query.get_attr_value(cluster, "#cluster_path")
    saver.writer(cluster_path, cluster)


def save_as(cluster: dict, cluster_path) -> None:
    saver.writer(cluster_path, cluster)


def unplug(cluster: dict) -> None:
    for gem, _ in gems_query.get_gems(cluster, None):
        global_ids_update.deindex(gem)
        global_tags_update.deindex(gem)


def build_aggregate() -> None:
    aggregate = {}
    base.set_aggregate(aggregate)


def create_resource_gem(resource_name: str, function: typing.Callable) -> dict:
    aggregate = base.get_aggregate()
    resources = make_gem(aggregate, aggregate, "Resources")
    group = resource_name.split(".")[0]
    resource_group_gem = make_gem(aggregate, resources, group)
    resource_gem = create_gem(aggregate, resource_group_gem, resource_name)
    attrs_update.set_function(resource_gem, function)
    return resource_gem


def get_resource_gem(resource_name: str) -> dict | None:
    aggregate = base.get_aggregate()
    resource_gem = local_ids_query.get_gem_by_gem_base_name(aggregate, resource_name)
    return resource_gem


def get_resource_description(resource_name: str) -> base.dict_keys | None:
    resource_gem = get_resource_gem(resource_name)
    if resource_gem is None:
        return None
    descriptions = global_tags_query.get_descriptions(resource_gem)
    return descriptions


def get_resource_function(resource_name: str) -> typing.Callable | None:
    resource_gem = get_resource_gem(resource_name)
    if resource_gem is None:
        return None
    function = attrs_query.get_function(resource_gem)
    return function


def initialize(home_path: pathlib.Path) -> None:
    build_aggregate()
