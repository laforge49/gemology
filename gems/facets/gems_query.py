from typing import *

from gems import base


def get_gf(gem: Optional[base.Gem]) -> Optional[base.GemsFacet]:
    if gem is None:
        return None
    facet = gem.get("GemsFacet")
    assert isinstance(facet, base.GemsFacet) or facet is None
    return facet


def get_gems(gem: Optional[base.Gem], gem_parent: Optional[base.Gem]):
    yield gem, gem_parent
    gf = get_gf(gem)
    if gf is not None:
        for child in gf:
            yield from get_gems(child, gem)
