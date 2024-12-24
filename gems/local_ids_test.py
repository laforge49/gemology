from gems import core, base
from gems.facets import local_ids_query
from pdml import saver


def test() -> None:
    print()
    print("*** local_ids_facet test ***")
    cluster1 = base.Cluster()
    gem1 = core.create_gem(cluster1, cluster1, "MyGem")
    print()
    print("cluster1:")
    saver.debug(cluster1)
    print()
    print("MyGem:")
    saver.debug(local_ids_query.cluster_get_gem_by_gem_base_name(cluster1, "MyGem"))
    cluster2 = base.Cluster()
    gem2 = core.create_gem(cluster2, cluster2, "Fred")
    print()
    print("cluster2:")
    saver.debug(cluster2)
    print()
    print("Fred")
    saver.debug(local_ids_query.cluster_get_gem_by_gem_base_name(cluster2, "Fred"))


if __name__ == "__main__":
    test()
