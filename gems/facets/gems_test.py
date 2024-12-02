from gems.facets import gems_update
from pdml import saver


def test() -> None:
    print()
    print("*** gems_facet test ***")
    parent_gem = {}
    child_gem = {}
    gems_update.add_child_gem(parent_gem, child_gem)
    print()
    print("parent gem:")
    saver.debug(parent_gem)
    print()
    print("child gem:")
    saver.debug(child_gem)


if __name__ == "__main__":
    test()
