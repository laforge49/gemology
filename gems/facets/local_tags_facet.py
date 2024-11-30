from gems import base
from gems.facets import attrs_facet


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


def make_ltf(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    ltf = get_ltf(gem)
    if ltf is None:
        ltf = {}
        gem["LocalTagsFacet"] = ltf
    return ltf


def get_ltif(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    cluster = attrs_facet.get_cluster(gem)
    return cluster.get("#LocalTagIndexFacet")


def cluster_get_tag_names(gem: dict | None) -> base.dict_keys | None:
    ltif = get_ltif(gem)
    if ltif is None:
        return None
    return ltif.keys()


def cluster_get_tag_values(gem: dict | None, id_type: str) -> base.dict_keys | None:
    ltif = get_ltif(gem)
    if ltif is None:
        return None
    ltif2 = ltif.get(id_type)
    if ltif2 is None:
        return None
    return ltif2.keys()
