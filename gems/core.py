import pathlib

from gems import base
from gems.facets import gems_query, local_ids_update, local_tags_update, attrs_update, global_ids_update, \
    global_tags_update, attrs_query, local_ids_query
from pdml import loader, saver


def create_gem(cluster: dict, gem_parent: dict, gem_base_name: str) -> dict:
    gem = {}
    attrs_update.set_cluster(gem, cluster)
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
    make_gem(aggregate, aggregate, "resources")
    base.set_aggregate(aggregate)


def add_function(function_name: str, function) -> None:
    resources = local_ids_query.get_gem_by_gem_base_name(base.get_aggregate(), "resources")
    af = attrs_update.make_af(resources)
    functions = af.get("functions")
    if functions is None:
        functions = {}
        af["functions"] = functions
    functions[function_name] = function


def get_function(function_name: str):
    resources = local_ids_query.get_gem_by_gem_base_name(base.get_aggregate(), "resources")
    functions = attrs_query.get_attr_value(resources, "functions")
    if functions is None:
        return None
    function = functions.get(function_name)
    return function


def initialize(home_path: pathlib.Path) -> None:
    build_aggregate()
