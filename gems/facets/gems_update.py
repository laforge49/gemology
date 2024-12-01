from gems.facets import gems_query
from pdml import saver


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
