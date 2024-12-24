from typing import *

from gems import base


def get_af(gem: Optional[base.Gem]) -> Optional[base.AttrsFacet]:
    if gem is None:
        return None
    facet = gem.get("AttrsFacet")
    assert isinstance(facet, base.AttrsFacet) or facet is None
    return facet


def get_attr_names(gem: Optional[base.Gem]) -> Optional[base.dict_keys]:
    af = get_af(gem)
    if af is None:
        return None
    return af.keys()


def get_attr_value(gem: Optional[base.Gem], attr_name: str) -> any:
    af = get_af(gem)
    if af is None:
        return None
    return af.get(attr_name)


def get_cluster(gem: Optional[base.Gem]) -> Optional[base.Cluster]:
    if gem is None:
        return None
    cluster = get_attr_value(gem, "#cluster")
    assert isinstance(cluster, base.Cluster) or cluster is None
    return cluster


def get_cluster_path(gem: Optional[base.Cluster]) -> Optional[str]:
    path = get_attr_value(gem, "#cluster_path")
    assert isinstance(path, str) or path is None
    return path


def get_gem_parent(gem: Optional[base.Gem]) -> Optional[base.Gem]:
    parent = get_attr_value(gem, "#gem_parent")
    assert isinstance(parent, base.Gem) or parent is None
    return parent


def get_function(gem: Optional[base.Gem]) -> Optional[Callable]:
    func = get_attr_value(gem, "#function")
    assert isinstance(func, Callable) or func is None
    return func


def get_class_name(gem: Optional[base.Gem]) -> Optional[str]:
    class_name = get_attr_value(gem, "ClassName")
    assert isinstance(class_name, str) or class_name is None
    return class_name
