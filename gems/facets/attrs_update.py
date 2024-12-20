from gems.facets import attrs_query, gems_update
import typing


def make_af(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    af = attrs_query.get_af(gem)
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
    af = attrs_query.get_af(gem)
    if af is None:
        return False
    attr_value = af.get(attr_name)
    if attr_value is None:
        return False
    del af[attr_name]
    return True


def set_cluster(gem: dict | None, cluster: dict) -> bool:
    return set_attr_value(gem, "#cluster", cluster)


def del_cluster_attr(gem: dict | None) -> bool:
    return del_attr(gem, "#cluster")


def set_cluster_path(cluster: dict | None, cluster_path: str) -> bool:
    return set_attr_value(cluster, "#cluster_path", cluster_path)


def del_cluster_path(cluster: dict | None) -> bool:
    return del_attr(cluster, "#cluster_path")


def set_gem_parent(gem: dict | None, gem_parent: dict) -> bool:
    return set_attr_value(gem, "#gem_parent", gem_parent)


def del_parent_attr(gem: dict | None) -> bool:
    return del_attr(gem, "#gem_parent")


def set_function(gem: dict | None, function: typing.Callable) -> bool:
    return set_attr_value(gem, "#function", function)


def create_gem(cluster: dict, gem_parent: dict) -> dict | None:
    gem = {}
    set_cluster(gem, cluster)
    gems_update.add_child_gem(gem_parent, gem)
    set_gem_parent(gem, gem_parent)
    return gem
