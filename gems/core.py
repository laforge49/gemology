import pathlib

from gems import base
from gems.facets import gems_query, local_ids_update, local_tags_update, attrs_update, global_ids_update, \
    global_tags_update, attrs_query
from pdml import loader, saver


def create_gem(cluster: dict, gem_parent: dict, gem_base_name: str) -> dict | None:
    gem = {}
    attrs_update.set_cluster(gem, cluster)
    attrs_update.set_gem_parent(gem, gem_parent)
    local_ids_update.set_gem_base_name(gem, gem_base_name)
    return gem


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


def test(home_path: pathlib.Path) -> None:
    print()
    print("*** core test ***")
    test_data_path = home_path / pathlib.Path("test data")
    print("test data path:", test_data_path)
    sample1 = load(test_data_path / pathlib.Path("sample1.pdml"))
    print()
    print("aggregate:")
    print(base.get_aggregate())
    saver.debug(base.get_aggregate())
    print()
    print("sample1")
    print(sample1)
    saver.debug(sample1)
    save_as(sample1, test_data_path / pathlib.Path("sample1a.pdml"))


if __name__ == "__main__":
    home_path = pathlib.Path.cwd()
    test(home_path)
