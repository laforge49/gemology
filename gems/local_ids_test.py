from gems.facets import local_ids_query, attrs_update, local_ids_update
from pdml import saver


def test() -> None:
    print()
    print("*** local_ids_facet test ***")
    cluster1 = {}
    gem1 = attrs_update.create_gem(cluster1, cluster1)
    local_ids_update.set_gem_base_name(gem1, "MyGem")
    print()
    print("cluster1:")
    saver.debug(cluster1)
    print()
    print("MyGem:")
    saver.debug(local_ids_query.get_gem_by_gem_base_name(cluster1, "MyGem"))
    cluster2 = {}
    gem2 = attrs_update.create_gem(cluster2, cluster2)
    lif = local_ids_update.make_lif(gem2)
    lif["gem_base_name"] = "Fred"
    local_ids_update.build_index(gem2)
    print()
    print("cluster2:")
    saver.debug(cluster2)
    print()
    print("Fred")
    saver.debug(local_ids_query.get_gem_by_gem_base_name(cluster2, "Fred"))


if __name__ == "__main__":
    test()
