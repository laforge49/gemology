from gems import base
from gems.facets import gems_facet
from pdml import saver


def get_af(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    return gem.get("AttrsFacet")


def get_attr_names(gem: dict | None) -> base.dict_keys | None:
    af = get_af(gem)
    if af is None:
        return None
    return af.keys()


def get_attr_value(gem: dict | None, attr_name: str) -> any:
    af = get_af(gem)
    if af is None:
        return None
    return af.get(attr_name)


def make_af(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    af = get_af(gem)
    if af is None:
        af = {}
        gem["AttrsFacet"] = af
    return af


def set_attr_value(gem: dict | None, attr_name: str, attr_value: any) -> bool:
    af = make_af(gem)
    if af is None:
        return False
    af[attr_name] = attr_value
    return True


def del_attr(gem: dict | None, attr_name: str) -> bool:
    af = get_af(gem)
    if af is None:
        return False
    attr_value = af.get(attr_name)
    if attr_value is None:
        return False
    del af[attr_name]
    return True


def get_cluster(gem: dict | None) -> dict | None:
    cluster = get_attr_value(gem, "#cluster")
    if cluster is None:
        cluster = gem
    return cluster


def set_cluster(gem: dict | None, cluster: dict) -> bool:
    return set_attr_value(gem, "#cluster", cluster)


def del_cluster_attr(gem: dict | None) -> bool:
    return del_attr(gem, "#cluster")


def get_cluster_path(gem: dict | None) -> str | None:
    return get_attr_value(gem, "#cluster_path")


def set_cluster_path(gem: dict | None, cluster_path: str) -> bool:
    return set_attr_value(gem, "#cluster_path", cluster_path)


def del_cluster_path_attr(gem: dict | None) -> bool:
    return del_attr(gem, "#cluster_path")


def get_gem_parent(gem: dict | None) -> dict | None:
    return get_attr_value(gem, "#gem_parent")


def set_gem_parent(gem: dict | None, gem_parent: dict) -> bool:
    gems_facet.add_child_gem(gem_parent, gem)
    return set_attr_value(gem, "#gem_parent", gem_parent)


def del_parent_attr(gem: dict | None) -> bool:
    return del_attr(gem, "#gem_parent")


def create_gem(cluster: dict, gem_parent: dict) -> dict | None:
    gem = {}
    set_cluster(gem, cluster)
    set_gem_parent(gem, gem_parent)
    return gem


def test() -> None:
    print()
    print("*** attrs_facet test ***")
    cluster = {}
    gem = create_gem(cluster, cluster)
    set_cluster_path(cluster, "fudge")
    del_cluster_path_attr(cluster)
    print()
    print("cluster:")
    saver.debug(cluster)
    print()
    print("gem:")
    saver.debug(gem)


if __name__ == "__main__":
    test()
