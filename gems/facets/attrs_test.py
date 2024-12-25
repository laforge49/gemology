from gems import core, base
from gems.facets import attrs_update
from pdml import saver


def test() -> None:
    print()
    print("*** attrs_facet test ***")
    cluster = base.Cluster()
    gem = core.make_gem(cluster, cluster, "cool")
    attrs_update.set_cluster_path(cluster, "fudge")
    attrs_update.del_cluster_path(cluster)
    print()
    print("cluster:")
    saver.debug(cluster)
    print()
    print("gem:")
    saver.debug(gem)


if __name__ == "__main__":
    test()
