def get_gf(gem: dict | None ) -> list | None:
    if gem is None:
        return None
    return gem.get("GemsFacet")


def make_gf(gem: dict | None) -> list | None:
    if gem is None:
        return None
    gf = get_gf(gem)
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
