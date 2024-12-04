from gems import base
from gems.facets import attrs_query, global_tags_query


def make_gtf(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    gtf = global_tags_query.get_gtf(gem)
    if gtf is None:
        gtf = {}
        gem["GlobalTagsFacet"] = gtf
    return gtf


def deindex_tag(gem: dict | None, tag_name: str, tag_value: str) -> bool:
    if gem is None:
        return False
    gtif = global_tags_query.get_gtif()
    if gtif is None:
        return False
    gtif2 = gtif.get(tag_name)
    if gtif2 is None:
        return False
    gems = gtif2.get(tag_value)
    if gems is None:
        return False
    return base.idremove(gems, gem)


def del_tag(gem: dict | None, tag_name: str, tag_value: str) -> bool:
    if gem is None:
        return False
    gtf = global_tags_query.get_gtf(gem)
    if gtf is None:
        return False
    values = gtf.get(tag_name)
    if values is None:
        return False
    if tag_value not in values:
        return False
    values.remove(tag_value)
    deindex_tag(gem, tag_name, tag_value)
    return True


def make_gtif() -> dict | None:
    gtif = global_tags_query.get_gtif()
    if gtif is None:
        gtif = {}
        aggregate = base.get_aggregate()
        aggregate["#GlobalTagIndexFacet"] = gtif
    return gtif


def make_gtif2(tag_name: str) -> dict | None:
    gtif = make_gtif()
    if gtif is None:
        return
    gtif2 = gtif.get(tag_name)
    if gtif2 is None:
        gtif2 = {}
        gtif[tag_name] = gtif2
    return gtif2


def set_tag(gem: dict | None, tag_name: str, tag_value: str) -> bool:
    if gem is None:
        return False
    gtf = make_gtf(gem)
    tag_values = gtf.get(tag_name)
    if tag_values is None:
        tag_values = []
        gtf[tag_name] = tag_values
    elif tag_value in tag_values:
        return False
    tag_values.append(tag_value)
    gtif2 = make_gtif2(tag_name)
    gems = gtif2.get(tag_value)
    if gems is None:
        gems = []
        gtif2[tag_value] = gems
    gems.append(gem)
    return True


def build_index(gem: dict) -> None:
    gtf = global_tags_query.get_gtf(gem)
    if gtf is None:
        return
    tag_names = gtf.keys()
    for tag_name in tag_names:
        tag_values = gtf.get(tag_name)
        if tag_values is not None:
            gtif2 = make_gtif2(tag_name)
            for tag_value in tag_values:
                gems = gtif2.get(tag_value)
                if gems is None:
                    gems = []
                    gtif2[tag_value] = gems
                if base.idindex(gems, gem) is None:
                    gems.append(gem)
