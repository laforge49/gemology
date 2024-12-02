from gems.facets import gems_query


def make_gf(gem: dict | None) -> list | None:
    if gem is None:
        return None
    gf = gems_query.get_gf(gem)
    if gf is None:
        gf = []
        gem["GemsFacet"] = gf
    return gf


def add_child_gem(gem: dict | None, child_gem: dict) -> bool:
    gf = make_gf(gem)
    if gf is None:
        return False
    gf.append(child_gem)
    return True
