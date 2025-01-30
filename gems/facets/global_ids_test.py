from gems import base, core
from gems.facets import global_ids_update, global_ids_query
from pdml import saver


def test() -> None:
    print()
    print("*** local_ids_facet test ***")
    core.build_aggregate()
    cluster1 = base.Cluster()
    global_ids_update.set_cluster_name(cluster1, base.ClusterName("Sam"))
    print()
    print("cluster1:")
    saver.debug(cluster1)
    print()
    print("Sam:")
    saver.debug(global_ids_query.get_cluster_by_cluster_name(base.ClusterName("Sam")))
    cluster2 = base.Cluster()
    gif = global_ids_update.make_gif(cluster2)
    gif["#cluster_name"] = "Sonny"
    global_ids_update.build_index(cluster2)
    print()
    print("cluster2:")
    saver.debug(cluster2)
    print()
    print("Sonny")
    saver.debug(global_ids_query.get_cluster_by_cluster_name(base.ClusterName("Sonny")))


if __name__ == "__main__":
    test()
