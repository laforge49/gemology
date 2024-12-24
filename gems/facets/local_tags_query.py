from typing import *


from gems import base


def get_ltf(gem: Optional[base.Gem]) -> Optional[base.LocalTagsFacet]:
    if gem is None:
        return None
    facet = gem.get("LocalTagsFacet")
    assert isinstance(facet, base.LocalTagsFacet) or facet is None
    return facet


def gem_get_tag_names(gem: Optional[base.Gem]) -> Optional[base.dict_keys]:
    ltf = get_ltf(gem)
    if ltf is None:
        return None
    return ltf.keys()


def gem_get_tag_value(gem: Optional[base.Gem], tag_name: str) -> any:
    ltf = get_ltf(gem)
    if ltf is None:
        return None
    return ltf.get(tag_name)


def cluster_get_ltif(cluster: Optional[base.Cluster]) -> Optional[dict]:
    if cluster is None:
        return None
    return cluster.get("#LocalTagIndexFacet")


def cluster_get_tag_names(cluster: Optional[base.Cluster]) -> Optional[base.dict_keys]:
    ltif = cluster_get_ltif(cluster)
    if ltif is None:
        return None
    return ltif.keys()


def cluster_get_tag_values(cluster: Optional[base.Cluster], tag_name: str) -> Optional[base.dict_keys]:
    ltif = cluster_get_ltif(cluster)
    if ltif is None:
        return None
    ltif2 = ltif.get(tag_name)
    if ltif2 is None:
        return None
    return ltif2.keys()


def cluster_get_gems_by_tag(cluster: Optional[base.Cluster], tag_name: str, tag_value: str) -> Optional[list]:
    ltif = cluster_get_ltif(cluster)
    if ltif is None:
        return None
    ltif2 = ltif.get(tag_name)
    if ltif2 is None:
        return None
    return ltif2.get(tag_value)
