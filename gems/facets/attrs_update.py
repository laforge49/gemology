from typing import *

from gems import base
from gems.facets import attrs_query, gems_update


def make_af(gem: Optional[base.Gem]) -> Optional[base.AttrsFacet]:
    if gem is None:
        return None
    af = attrs_query.get_af(gem)
    if af is None:
        af = base.AttrsFacet()
        gem["AttrsFacet"] = af
    assert isinstance(af, base.AttrsFacet)
    return af


def set_attr_value(gem: Optional[base.Gem], attr_name: str, attr_value: any) -> bool:
    af = make_af(gem)
    if af is None:
        return False
    af[attr_name] = attr_value
    return True


def del_attr(gem: Optional[base.Gem], attr_name: str) -> bool:
    af = attrs_query.get_af(gem)
    if af is None:
        return False
    attr_value = af.get(attr_name)
    if attr_value is None:
        return False
    del af[attr_name]
    return True


def set_cluster(gem: Optional[base.Gem], cluster: base.Cluster) -> bool:
    return set_attr_value(gem, "#cluster", cluster)


def del_cluster_attr(gem: Optional[base.Gem]) -> bool:
    return del_attr(gem, "#cluster")


def set_cluster_path(cluster: Optional[base.Cluster], cluster_path: str) -> bool:
    return set_attr_value(cluster, "#cluster_path", cluster_path)


def del_cluster_path(cluster: Optional[base.Cluster]) -> bool:
    return del_attr(cluster, "#cluster_path")


def set_gem_parent(gem: Optional[base.Gem], gem_parent: base.Gem) -> bool:
    assert isinstance(gem_parent, base.Gem)
    return set_attr_value(gem, "#gem_parent", gem_parent)


def del_parent_attr(gem: Optional[base.Gem]) -> bool:
    return del_attr(gem, "#gem_parent")


def set_function(gem: Optional[base.Gem], function: Callable) -> bool:
    return set_attr_value(gem, "#function", function)


def set_class_name(gem: Optional[base.Gem], function: str) -> bool:
    return set_attr_value(gem, "ClassName", function)
