from gems import base
from gems.facets import attrs_query


def get_ltf(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    return gem.get("LocalTagsFacet")


def gem_get_tag_names(gem: dict | None) -> base.dict_keys | None:
    ltf = get_ltf(gem)
    if ltf is None:
        return None
    return ltf.keys()


def gem_get_tag_values(gem: dict | None, tag_name: str) -> list | None:
    ltf = get_ltf(gem)
    if ltf is None:
        return None
    return ltf.get(tag_name)


def get_ltif(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    cluster = attrs_query.get_cluster(gem)
    return cluster.get("#LocalTagIndexFacet")


def cluster_get_tag_names(cluster: dict | None) -> base.dict_keys | None:
    ltif = get_ltif(cluster)
    if ltif is None:
        return None
    return ltif.keys()


def cluster_get_tag_values(cluster: dict | None, tag_name: str) -> base.dict_keys | None:
    ltif = get_ltif(cluster)
    if ltif is None:
        return None
    ltif2 = ltif.get(tag_name)
    if ltif2 is None:
        return None
    return ltif2.keys()


def cluster_get_gems_by_tag(cluster: dict | None, tag_name: str, tag_value: str) -> list | None:
    ltif = get_ltif(cluster)
    if ltif is None:
        return None
    ltif2 = ltif.get(tag_name)
    if ltif2 is None:
        return None
    return ltif2.get(tag_value)
