from gems import base


def get_gtf(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    return gem.get("GlobalTagsFacet")


def gem_get_tag_names(gem: dict | None) -> base.dict_keys | None:
    gtf = get_gtf(gem)
    if gtf is None:
        return None
    return gtf.keys()


def gem_get_tag_values(gem: dict | None, tag_name: str) -> list | None:
    gtf = get_gtf(gem)
    if gtf is None:
        return None
    return gtf.get(tag_name)


def get_gtif() -> dict | None:
    aggregate = base.get_aggregate()
    return aggregate.get("#GlobalTagIndexFacet")


def aggregate_get_tag_names() -> base.dict_keys | None:
    gtif = get_gtif()
    if gtif is None:
        return None
    return gtif.keys()


def aggregate_get_tag_values(tag_name: str) -> base.dict_keys | None:
    gtif = get_gtif()
    if gtif is None:
        return None
    gtif2 = gtif.get(tag_name)
    if gtif2 is None:
        return None
    return gtif2.keys()


def aggregate_get_gems_by_tag(tag_name: str, tag_value: str) -> list | None:
    gtif = get_gtif()
    if gtif is None:
        return None
    gtif2 = gtif.get(tag_name)
    if gtif2 is None:
        return None
    return gtif2.get(tag_value)
