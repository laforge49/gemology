from typing import *

from gems import base


def get_af(gem: Optional[base.Gem]) -> Optional[dict]:
    if gem is None:
        return None
    facet = gem.get("AttrsFacet")
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
    cluster = get_attr_value(gem, "#cluster")
    if cluster is None:
        cluster = gem
    assert isinstance(cluster, base.Cluster)
    return cluster


def get_cluster_path(gem: Optional[base.Cluster]) -> Optional[str]:
    path = get_attr_value(gem, "#cluster_path")
    assert isinstance(path, str)
    return path


def get_gem_parent(gem: Optional[Type[base.Gem]]) -> dict | None:
    return get_attr_value(gem, "#gem_parent")


def get_function(gem: Optional[Type[base.Gem]]) -> Optional[Callable]:
    return get_attr_value(gem, "#function")


def get_class_name(gem: Optional[Type[base.Gem]]) -> Optional[str]:
    return get_attr_value(gem, "ClassName")
