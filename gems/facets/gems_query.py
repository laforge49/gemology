from typing import *

from gems import base


def get_gf(gem: Optional[base.Gem]) -> Optional[list]:
    if gem is None:
        return None
    return gem.get("GemsFacet")


def get_gems(gem: Optional[base.Gem], gem_parent: Optional[base.Gem]):
    yield gem, gem_parent
    gf = get_gf(gem)
    if gf is not None:
        for child in gf:
            yield from get_gems(child, gem)
