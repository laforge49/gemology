from typing import *


from gems import base
from gems.facets import global_tags_query


def make_gtf(gem: Optional[base.Gem]) -> Optional[base.GlobalTagsFacet]:
    if gem is None:
        return None
    gtf = global_tags_query.get_gtf(gem)
    if gtf is None:
        gtf = base.GlobalTagsFacet()
        gem["GlobalTagsFacet"] = gtf
    assert isinstance(gtf, base.GlobalTagsFacet)
    return gtf


def deindex_tag(gem: Optional[base.Gem], tag_name: str, tag_value: str) -> bool:
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


def del_tag(gem: Optional[base.Gem], tag_name: str) -> bool:
    if gem is None:
        return False
    gtf = global_tags_query.get_gtf(gem)
    if gtf is None:
        return False
    tag_value: str = gtf.get(tag_name)
    if tag_value is None:
        return False
    del gtf[tag_name]
    deindex_tag(gem, tag_name, tag_value)
    return True


def make_gtif() -> Optional[dict]:
    gtif = global_tags_query.get_gtif()
    if gtif is None:
        gtif = {}
        aggregate = base.get_aggregate()
        aggregate["#GlobalTagIndexFacet"] = gtif
    return gtif


def make_gtif2(tag_name: str) -> Optional[dict]:
    gtif = make_gtif()
    gtif2 = gtif.get(tag_name)
    if gtif2 is None:
        gtif2 = {}
        gtif[tag_name] = gtif2
    return gtif2


def set_tag(gem: Optional[base.Gem], tag_name: str, tag_value: str) -> bool:
    if gem is None:
        return False
    gtf = make_gtf(gem)
    value = gtf.get(tag_name)
    if value == tag_value:
        return False
    gtf[tag_name] = tag_value
    gtif2 = make_gtif2(tag_name)
    gems = gtif2.get(value)
    if gems:
        gems.remove(gem)
    if gems is None:
        gems = []
        gtif2[tag_value] = gems
    gems.append(gem)
    return True


def build_index(gem: Optional[base.Gem]) -> None:
    gtf = global_tags_query.get_gtf(gem)
    if gtf is None:
        return
    tag_names = gtf.keys()
    for tag_name in tag_names:
        tag_value = gtf.get(tag_name)
        if tag_value is not None:
            gtif2 = make_gtif2(tag_name)
            gems = gtif2.get(tag_value)
            if gems is None:
                gems = []
                gtif2[tag_value] = gems
            if base.idindex(gems, gem) is None:
                gems.append(gem)


def deindex(gem: Optional[base.Gem]) -> None:
    gtf = global_tags_query.get_gtf(gem)
    if gtf is None:
        return
    gtif = global_tags_query.get_gtif()
    if gtif is None:
        return
    tag_names = gtf.keys()
    for tag_name in tag_names:
        gtif2 = gtif.get(tag_name)
        tag_value = gtf.get(tag_name)
        if gtif2 and tag_value:
            gems = gtif2.get(tag_value)
            base.idremove(gems, gem)


def del_description(gem: Optional[base.Gem]) -> bool:
    return del_tag(gem, "description")


def set_description(gem: Optional[base.Gem], description: str) -> bool:
    return set_tag(gem, "description", description)
