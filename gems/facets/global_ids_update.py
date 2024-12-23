from typing import *


from gems import base
from gems.facets import global_ids_query


def make_gif(gem: Optional[base.Gem]) -> dict | None:
    if gem is None:
        return None
    gif = global_ids_query.get_gif(gem)
    if gif is None:
        gif = {}
        gem["GlobalIdsFacet"] = gif
    return gif


def deindex_id(id_type: str, id_name: str) -> bool:
    giif = global_ids_query.get_giif()
    if giif is None:
        return False
    giif2 = giif.get(id_type)
    if giif2 is None:
        return False
    if giif2.get(id_name) is None:
        return False
    del giif2[id_name]
    return True


def del_id(gem: Optional[base.Gem], id_type: str, id_name: str) -> bool:
    if gem is None:
        return False
    gif = global_ids_query.get_gif(gem)
    if gif is None:
        return False
    if gif.get(id_type) is None:
        return False
    deindex_id(id_type, id_name)
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


def set_id(gem: Optional[base.Gem], id_type: str, id_name: str) -> bool:
    if gem is None:
        return False
    del_id(gem, id_type, id_name)
    gif = make_gif(gem)
    gif[id_type] = id_name
    giif2 = make_giif2(id_type)
    giif2[id_name] = gem
    return True


def build_index(gem: Optional[base.Gem]) -> None:
    gif = global_ids_query.get_gif(gem)
    if gif is None:
        return
    id_types = gif.keys()
    for id_type in id_types:
        id_name = gif.get(id_type)
        if id_name:
            giif2 = make_giif2(id_type)
            giif2[id_name] = gem


def deindex(gem: Optional[base.Gem]) -> None:
    gif = global_ids_query.get_gif(gem)
    if gif is None:
        return
    giif = global_ids_query.get_giif()
    if giif is None:
        return
    id_types = gif.keys()
    for id_type in id_types:
        giif2 = giif.get(id_type)
        id_name = gif.get(id_type)
        if giif2 and id_name and giif2.get(id_name):
            del giif2[id_name]


def del_cluster_name(cluster: Optional[base.Cluster], id_name: str) -> bool:
    return del_id(cluster, "#cluster_name", id_name)


def set_cluster_name(cluster: Optional[base.Cluster], cluster_name: str) -> bool:
    return set_id(cluster, "#cluster_name", cluster_name)
