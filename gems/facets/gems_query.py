def get_gf(gem: dict | None ) -> list | None:
    if gem is None:
        return None
    return gem.get("GemsFacet")


def get_gems(gem: dict):
    yield gem
    gf = get_gf(gem)
    if gf is not None:
        for child in gf:
            yield from get_gems(child)
