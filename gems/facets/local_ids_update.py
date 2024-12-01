from gems.facets import local_ids_query, attrs_query, attrs_update
from pdml import saver


def make_lif(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    lif = local_ids_query.get_lif(gem)
    if lif is None:
        lif = {}
        gem["LocalIdsFacet"] = lif
    return lif


def del_id(gem: dict | None, id_type: str, id_name: str) -> bool:
    if gem is None:
        return False
    lif = local_ids_query.get_lif(gem)
    if lif is None:
        return False
    if lif.get(id_type) is None:
        return False
    del lif[id_type]
    liif = local_ids_query.get_liif(gem)
    liif2 = liif.get(id_type)
    del liif2[id_name]
    return True


def make_liif(gem: dict | None) -> dict | None:
    cluster = attrs_query.get_cluster(gem)
    if cluster is None:
        return None
    liif = local_ids_query.get_liif(cluster)
    if liif is None:
        liif = {}
        cluster["#LocalIdIndexFacet"] = liif
    return liif


def make_liif2(gem: dict | None, id_type: str) -> dict | None:
    liif = make_liif(gem)
    if liif is None:
        return
    liif2 = liif.get(id_type)
    if liif2 is None:
        liif2 = {}
        liif[id_type] = liif2
    return liif2


def set_id(gem: dict | None, id_type: str, id_name: str) -> bool:
    if gem is None:
        return False
    del_id(gem, id_type, id_name)
    lif = make_lif(gem)
    lif[id_type] = id_name
    liif2 = make_liif2(gem, id_type)
    liif2[id_name] = gem
    return True


def build_index(gem: dict) -> None:
    lif = local_ids_query.get_lif(gem)
    if lif is None:
        return
    id_types = lif.keys()
    for id_type in id_types:
        id_name = lif.get(id_type)
        liif2 = make_liif2(gem, id_type)
        liif2[id_name] = gem


def del_gem_base_name(gem: dict | None, id_name: str) -> bool:
    return del_id(gem, "gem_base_name", id_name)


def set_gem_base_name(gem: dict | None, gem_base_name: str) -> bool:
    return set_id(gem, "gem_base_name", gem_base_name)


def test() -> None:
    print()
    print("*** local_ids_facet test ***")
    cluster1 = {}
    gem1 = attrs_update.create_gem(cluster1, cluster1)
    set_gem_base_name(gem1, "MyGem")
    print()
    print("cluster1:")
    saver.debug(cluster1)
    print()
    print("MyGem:")
    saver.debug(local_ids_query.get_gem_by_gem_base_name(cluster1, "MyGem"))
    cluster2 = {}
    gem2 = attrs_update.create_gem(cluster2, cluster2)
    lif = make_lif(gem2)
    lif["gem_base_name"] = "Fred"
    build_index(gem2)
    print()
    print("cluster2:")
    saver.debug(cluster2)
    print()
    print("Fred")
    saver.debug(local_ids_query.get_gem_by_gem_base_name(cluster2, "Fred"))


if __name__ == "__main__":
    test()
