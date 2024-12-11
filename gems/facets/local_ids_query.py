from gems import base
from gems.facets import attrs_query
from pdml import saver


def get_lif(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    return gem.get("LocalIdsFacet")


def gem_get_id_types(gem: dict | None) -> base.dict_keys | None:
    lif = get_lif(gem)
    if lif is None:
        return None
    return lif.keys()


def gem_get_id_name(gem: dict | None, id_type: str) -> str | None:
    lif = get_lif(gem)
    if lif is None:
        return None
    return lif.get(id_type)


def get_liif(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    cluster = attrs_query.get_cluster(gem)
    return cluster.get("#LocalIdIndexFacet")


def cluster_get_id_types(gem: dict | None) -> base.dict_keys | None:
    liif = get_liif(gem)
    if liif is None:
        return None
    return liif.keys()


def cluster_get_id_names(cluster: dict | None, id_type: str) -> base.dict_keys | None:
    liif = get_liif(cluster)
    if liif is None:
        return None
    liif2 = liif.get(id_type)
    if liif2 is None:
        return None
    return liif2.keys()


def cluster_get_gem_by_id(cluster: dict | None, id_type: str, id_name: str) -> dict | None:
    liif = get_liif(cluster)
    if liif is None:
        return None
    liif2 = liif.get(id_type)
    if liif2 is None:
        return None
    return liif2.get(id_name)


def get_gem_base_name(gem: dict | None) -> str | None:
    return gem_get_id_name(gem, "gem_base_name")


def cluster_get_gem_base_names(cluster: dict | None) -> base.dict_keys | None:
    return cluster_get_id_names(cluster, "gem_base_name")


def get_gem_by_gem_base_name(cluster: dict | None, gem_base_name: str) -> dict | None:
    return cluster_get_gem_by_id(cluster, "gem_base_name", gem_base_name)
