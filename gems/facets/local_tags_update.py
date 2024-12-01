from gems import base
from gems.facets import attrs_query, local_tags_query


def make_ltf(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    ltf = local_tags_query.get_ltf(gem)
    if ltf is None:
        ltf = {}
        gem["LocalTagsFacet"] = ltf
    return ltf


def del_tag(gem: dict | None, tag_name: str, tag_value: str) -> bool:
    if gem is None:
        return False
    ltf = local_tags_query.get_ltf(gem)
    if ltf is None:
        return False
    values = ltf.get(tag_name)
    if values is None:
        return False
    if tag_value not in values:
        return False
    values.remove(tag_value)
    ltif = local_tags_query.get_ltif(gem)
    ltif2 = ltif.get(tag_name)
    gems = ltif2.get(tag_value)
    base.idremove(gems, gem)
    return True


def make_ltif(gem: dict | None) -> dict | None:
    cluster = attrs_query.get_cluster(gem)
    if cluster is None:
        return None
    ltif = local_tags_query.get_ltif(cluster)
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
    ltf = local_tags_query.get_ltf(gem)
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
