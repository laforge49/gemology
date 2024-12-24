from typing import *


from gems import base


def get_gtf(gem: Optional[base.Gem]) -> Optional[base.GlobalTagsFacet]:
    if gem is None:
        return None
    facet = gem.get("GlobalTagsFacet")
    assert isinstance(facet, base.GlobalTagsFacet) or facet is None
    return facet


def gem_get_tag_names(gem: Optional[base.Gem]) -> Optional[base.dict_keys]:
    gtf = get_gtf(gem)
    if gtf is None:
        return None
    return gtf.keys()


def gem_get_tag_value(gem: Optional[base.Gem], tag_name: str) -> any:
    gtf = get_gtf(gem)
    if gtf is None:
        return None
    return gtf.get(tag_name)


def get_gtif() -> Optional[base.GlobalTagIndexFacet]:
    aggregate = base.get_aggregate()
    gtif = aggregate.get("#GlobalTagIndexFacet")
    assert isinstance(gtif, base.GlobalTagIndexFacet) or gtif is None
    return gtif


def aggregate_get_tag_names() -> Optional[base.dict_keys]:
    gtif = get_gtif()
    if gtif is None:
        return None
    return gtif.keys()


def aggregate_get_tag_values(tag_name: str) -> Optional[base.dict_keys]:
    gtif = get_gtif()
    if gtif is None:
        return None
    gtif2 = gtif.get(tag_name)
    if gtif2 is None:
        return None
    return gtif2.keys()


def aggregate_get_gems_by_tag(tag_name: str, tag_value: str) -> Optional[list]:
    gtif = get_gtif()
    if gtif is None:
        return None
    gtif2 = gtif.get(tag_name)
    if gtif2 is None:
        return None
    return gtif2.get(tag_value)


def get_descriptions(gem: Optional[base.Gem]) -> Optional[base.dict_keys]:
    return gem_get_tag_value(gem, "description")


def aggregate_get_descriptions() -> Optional[base.dict_keys]:
    return aggregate_get_tag_values("description")


def get_gems_by_description(description: str) -> Optional[list]:
    return aggregate_get_gems_by_tag("description", description)
