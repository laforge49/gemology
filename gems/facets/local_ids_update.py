from typing import *

from gems import base
from gems.facets import local_ids_query, attrs_query


def make_lif(gem: Optional[base.Gem]) -> Optional[base.LocalIdsFacet]:
    if gem is None:
        return None
    lif = local_ids_query.get_lif(gem)
    if lif is None:
        lif = base.LocalIdsFacet()
        gem["LocalIdsFacet"] = lif
    assert isinstance(lif, base.LocalIdsFacet)
    return lif


def del_id(gem: Optional[base.Gem], id_type: str, id_name: str) -> bool:
    if gem is None:
        return False
    lif = local_ids_query.get_lif(gem)
    if lif is None:
        return False
    if lif.get(id_type) is None:
        return False
    del lif[id_type]
    cluster = attrs_query.get_cluster(gem)
    if cluster is None:
        return False
    liif = local_ids_query.cluster_get_liif(cluster)
    liif2 = liif.get(id_type)
    del liif2[id_name]
    return True


def cluster_make_liif(cluster: Optional[base.Cluster]) -> Optional[dict]:
    liif = local_ids_query.cluster_get_liif(cluster)
    if liif is None:
        liif = {}
        cluster["#LocalIdIndexFacet"] = liif
    return liif


def cluster_make_liif2(cluster: Optional[base.Cluster], id_type: str) -> Optional[dict]:
    liif = cluster_make_liif(cluster)
    if liif is None:
        return
    liif2 = liif.get(id_type)
    if liif2 is None:
        liif2 = {}
        liif[id_type] = liif2
    return liif2


def set_id(gem: Optional[base.Gem], id_type: str, id_name: str) -> bool:
    if gem is None:
        return False
    del_id(gem, id_type, id_name)
    lif = make_lif(gem)
    if lif is None:
        return False
    lif[id_type] = id_name
    cluster = attrs_query.get_cluster(gem)
    if cluster is None:
        return False
    liif2 = cluster_make_liif2(cluster, id_type)
    if liif2 is None:
        return False
    liif2[id_name] = gem
    return True


def build_index(gem: Optional[base.Gem]) -> bool:
    lif = local_ids_query.get_lif(gem)
    if lif is None:
        return False
    id_types = lif.keys()
    cluster = attrs_query.get_cluster(gem)
    if cluster is None:
        return False
    for id_type in id_types:
        id_name = lif.get(id_type)
        liif2 = cluster_make_liif2(cluster, id_type)
        if liif2 is None:
            return False
        liif2[id_name] = gem
    return True


def del_gem_base_name(gem: Optional[base.Gem], id_name: str) -> bool:
    return del_id(gem, "gem_base_name", id_name)


def set_gem_base_name(gem: Optional[base.Gem], gem_base_name: str) -> bool:
    return set_id(gem, "gem_base_name", gem_base_name)
