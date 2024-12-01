from gems.facets import gems_query, attrs_query, local_ids_query, local_tags_query
from pdml import saver


def build_indexes(cluster: dict) -> None:
    for gem in gems_facet.get_gems(cluster):
        local_ids_facet.build_index(gem)
        local_tags_facet.build_index(gem)


def test() -> None:
    print()
    print("*** core test ***")
    cluster2 = {}
    gem2 = attrs_facet.create_gem(cluster2, cluster2)
    lif = local_ids_facet.make_lif(gem2)
    lif["gem_base_name"] = "Fred"
    build_indexes(cluster2)
    print()
    print("cluster2:")
    saver.debug(cluster2)
    print()
    print("Fred")
    saver.debug(local_ids_facet.get_gem_by_gem_base_name(cluster2, "Fred"))


if __name__ == "__main__":
    test()
