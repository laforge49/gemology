from gems import core
from gems.facets import attrs_update, local_ids_query, local_ids_update
from pdml import saver


def test() -> None:
    print()
    print("*** core test ***")
    cluster2 = {}
    gem2 = attrs_update.create_gem(cluster2, cluster2)
    lif = local_ids_update.make_lif(gem2)
    lif["gem_base_name"] = "Fred"
    core.build_indexes(cluster2)
    print()
    print("cluster2:")
    saver.debug(cluster2)
    print()
    print("Fred")
    saver.debug(local_ids_query.get_gem_by_gem_base_name(cluster2, "Fred"))


if __name__ == "__main__":
    test()
