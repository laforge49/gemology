from pdml import saver


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


def get_gems(gem: dict):
    yield gem
    gf = get_gf(gem)
    if gf is not None:
        for child in gf:
            yield from get_gems(child)


def test() -> None:
    print()
    print("*** gems_facet test ***")
    parent_gem = {}
    child_gem = {}
    add_child_gem(parent_gem, child_gem)
    print()
    print("parent gem:")
    saver.debug(parent_gem)
    print()
    print("child gem:")
    saver.debug(child_gem)


if __name__ == "__main__":
    test()
