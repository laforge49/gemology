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
    base.idremove(gems, gem)
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
    ltf = make_ltf(gem)
    tag_values = ltf.get(tag_name)
    if tag_values is None:
        tag_values = []
        ltf[tag_name] = tag_values
    elif tag_value in tag_values:
        return False
    tag_values.append(tag_value)
    ltif2 = make_ltif2(gem, tag_name)
    gems = ltif2.get(tag_value)
    if gems is None:
        gems = []
        ltif2[tag_value] = gems
    gems.append(gem)
    return True


def build_index(gem: dict) -> None:
    ltf = get_ltf(gem)
    if ltf is None:
        return
    tag_names = ltf.keys()
    for tag_name in tag_names:
        tag_values = ltf.get(tag_name)
        if tag_values is not None:
            ltif2 = make_ltif2(gem, tag_name)
            for tag_value in tag_values:
                gems = ltif2.get(tag_value)
                if gems is None:
                    gems = []
                    ltif2[tag_value] = gems
                if base.idindex(gems, gem) is None:
                    gems.append(gem)


def get_facet_names(gem: dict | None) -> list | None:
    return gem_get_tag_values(gem, "#facet_names")


def get_gems_by_facet_name(gem: dict | None, facet_name: str) -> list | None:
    return cluster_get_gems_by_tag(gem, "#facet_names", facet_name)


def del_facet_name(gem: dict | None, facet_name: str) -> bool:
    return del_tag(gem, "#facet_names", facet_name)


def set_facet_name(gem: dict | None, facet_name: str) -> bool:
    return set_tag(gem, "#facet_names", facet_name)
