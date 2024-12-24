from typing import *


from gems import base


def get_lif(gem: Optional[base.Gem]) -> Optional[base.LocalIdsFacet]:
    if gem is None:
        return None
    facet = gem.get("LocalIdsFacet")
    assert isinstance(facet, base.LocalIdsFacet) or facet is None
    return facet


def gem_get_id_types(gem: Optional[base.Gem]) -> Optional[base.dict_keys]:
    lif = get_lif(gem)
    if lif is None:
        return None
    return lif.keys()


def gem_get_id_name(gem: Optional[base.Gem], id_type: str) -> Optional[str]:
    lif = get_lif(gem)
    if lif is None:
        return None
    return lif.get(id_type)


def cluster_get_liif(cluster: Optional[base.Cluster]) -> Optional[base.LocalIdIndexFacet]:
    if cluster is None:
        return None
    liif = cluster.get("#LocalIdIndexFacet")
    assert isinstance(liif, base.LocalIdIndexFacet) or liif is None
    return liif


def cluster_get_id_types(cluster: Optional[base.Cluster]) -> Optional[base.dict_keys]:
    liif = cluster_get_liif(cluster)
    if liif is None:
        return None
    return liif.keys()


def cluster_get_id_names(cluster: Optional[base.Cluster], id_type: str) -> Optional[base.dict_keys]:
    liif = cluster_get_liif(cluster)
    if liif is None:
        return None
    liif2 = liif.get(id_type)
    if liif2 is None:
        return None
    return liif2.keys()


def cluster_get_gem_by_id(cluster: Optional[base.Cluster], id_type: str, id_name: str) -> Optional[base.Gem]:
    liif = cluster_get_liif(cluster)
    if liif is None:
        return None
    liif2 = liif.get(id_type)
    if liif2 is None:
        return None
    return liif2.get(id_name)


def get_gem_base_name(gem: Optional[base.Gem]) -> Optional[str]:
    return gem_get_id_name(gem, "gem_base_name")


def cluster_get_gem_base_names(cluster: Optional[base.Cluster]) -> Optional[base.dict_keys]:
    return cluster_get_id_names(cluster, "gem_base_name")


def cluster_get_gem_by_gem_base_name(cluster: Optional[base.Cluster], gem_base_name: str) -> Optional[base.Gem]:
    return cluster_get_gem_by_id(cluster, "gem_base_name", gem_base_name)
