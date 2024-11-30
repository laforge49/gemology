from gems import base
from gems.facets import attrs_facet


def get_ltf(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    return gem.get("LocalTagsFacet")


def get_tag_names(gem: dict | None) -> base.dict_keys | None:
    ltf = get_ltf(gem)
    if ltf is None:
        return None
    return ltf.keys()


def get_tag_values(gem: dict | None, tag_name: str) -> list | None:
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
