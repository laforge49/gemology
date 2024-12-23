from gems import core, base
from gems.facets import local_ids_query
from pdml import saver


def test() -> None:
    print()
    print("*** core test ***")
    cluster2 = base.Cluster()
    gem2 = core.create_gem(cluster2, cluster2, "Fred")
    print()
    print("cluster2:")
    saver.debug(cluster2)
    print()
    print("Fred")
    saver.debug(local_ids_query.get_gem_by_gem_base_name(cluster2, "Fred"))


if __name__ == "__main__":
    test()
