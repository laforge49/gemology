dict_keys = type({}.keys())


def get_gf(gem: dict | None ) -> list | None:
    if gem is None:
        return None
    return gem.get("GemsFacet")


def make_gf(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    gf = get_gf(gem)
    if gf is None:
        gf = {}
        gem["GemsFacet"] = gf
    return gf
