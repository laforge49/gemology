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


def cluster_get_tag_values(gem: dict | None, tag_name: str) -> base.dict_keys | None:
    ltif = get_ltif(gem)
    if ltif is None:
        return None
    ltif2 = ltif.get(tag_name)
    if ltif2 is None:
        return None
    return ltif2.keys()


def cluster_get_gems_by_tag(gem: dict | None, tag_name: str, tag_value: str) -> list | None:
    ltif = get_ltif(gem)
    if ltif is None:
        return None
    ltif2 = ltif.get(tag_name)
    if ltif2 is None:
        return None
    return ltif2.get(tag_value)


def del_tag(gem: dict | None, tag_name: str, tag_value: str) -> bool:
    if gem is None:
        return False
    ltf = get_ltf(gem)
    if ltf is None:
        return False
    values = ltf.get(tag_name)
    if values is None:
        return False
    if tag_value not in values:
        return False
    values.remove(tag_value)
    ltif = get_ltif(gem)
    ltif2 = ltif.get(tag_name)
    gems = ltif2.get(tag_value)
    gems.remove(gem)
    return True


def make_ltif(gem: dict | None) -> dict | None:
    cluster = attrs_facet.get_cluster(gem)
    if cluster is None:
        return None
    ltif = get_ltif(cluster)
    if ltif is None:
        ltif = {}
        cluster["#LocalTagIndexFacet"] = ltif
    return ltif


def make_ltif2(gem: dict | None, tag_name: str) -> dict | None:
    ltif = make_ltif(gem)
    if ltif is None:
        return
    ltif2 = ltif.get(tag_name)
    if ltif2 is None:
        ltif2 = {}
        ltif[tag_name] = ltif2
    return ltif2


def set_tag(gem: dict | None, tag_name: str, tag_value: str) -> bool:
    if gem is None:
        return False
    del_tag(gem, tag_name, tag_value)
    ltf = make_ltf(gem)
    ltf[tag_name] = tag_value
    ltif2 = make_ltif2(gem, tag_name)
    ltif2[tag_value] = gem
    return True
