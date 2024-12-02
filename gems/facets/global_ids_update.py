from gems import base
from gems.facets import global_ids_query, attrs_query, attrs_update
from pdml import saver


def make_gif(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    gif = global_ids_query.get_gif(gem)
    if gif is None:
        gif = {}
        gem["GlobalIdsFacet"] = gif
    return gif


def del_id(gem: dict | None, id_type: str, id_name: str) -> bool:
    if gem is None:
        return False
    gif = global_ids_query.get_gif(gem)
    if gif is None:
        return False
    if gif.get(id_type) is None:
        return False
    del gif[id_type]
    giif = global_ids_query.get_giif()
    giif2 = giif.get(id_type)
    del giif2[id_name]
    return True


def make_giif() -> dict | None:
    giif = global_ids_query.get_giif()
    if giif is None:
        giif = {}
        aggregate = base.get_aggregate()
        aggregate["#GlobalIdIndexFacet"] = giif
    return giif


def make_giif2(id_type: str) -> dict | None:
    giif = make_giif()
    if giif is None:
        return
    giif2 = giif.get(id_type)
    if giif2 is None:
        giif2 = {}
        giif[id_type] = giif2
    return giif2


def set_id(gem: dict | None, id_type: str, id_name: str) -> bool:
    if gem is None:
        return False
    del_id(gem, id_type, id_name)
    gif = make_gif(gem)
    gif[id_type] = id_name
    giif2 = make_giif2(id_type)
    giif2[id_name] = gem
    return True


def build_index(gem: dict) -> None:
    gif = global_ids_query.get_gif(gem)
    if gif is None:
        return
    id_types = gif.keys()
    for id_type in id_types:
        id_name = gif.get(id_type)
        giif2 = make_giif2(id_type)
        giif2[id_name] = gem


def del_cluster_name(gem: dict | None, id_name: str) -> bool:
    return del_id(gem, "#cluster_name", id_name)


def set_cluster_name(gem: dict | None, cluster_name: str) -> bool:
    return set_id(gem, "#cluster_name", cluster_name)


def test() -> None:
    print()
    print("*** local_ids_facet test ***")
    cluster1 = {}
    set_cluster_name(cluster1, "Sam")
    print()
    print("cluster1:")
    saver.debug(cluster1)
    print()
    print("Sam:")
    saver.debug(global_ids_query.get_cluster_by_cluster_name("Sam"))
    cluster2 = {}
    gif = make_gif(cluster2)
    gif["#cluster_name"] = "Sonny"
    build_index(cluster2)
    print()
    print("cluster2:")
    saver.debug(cluster2)
    print()
    print("Sonny")
    saver.debug(global_ids_query.get_cluster_by_cluster_name("Sonny"))


if __name__ == "__main__":
    test()
