from typing import *


from gems import base


def get_gif(gem: Optional[base.Gem]) -> Optional[dict]:
    if gem is None:
        return None
    return gem.get("GlobalIdsFacet")


def gem_get_id_types(gem: Optional[base.Gem]) -> Optional[base.dict_keys]:
    gif = get_gif(gem)
    if gif is None:
        return None
    return gif.keys()


def gem_get_id_name(gem: Optional[base.Gem], id_type: str) -> Optional[str]:
    gif = get_gif(gem)
    if gif is None:
        return None
    return gif.get(id_type)


def get_giif() -> Optional[dict]:
    aggregate = base.get_aggregate()
    return aggregate.get("#GlobalIdIndexFacet")


def aggregate_get_id_types() -> Optional[base.dict_keys]:
    giif = get_giif()
    if giif is None:
        return None
    return giif.keys()


def aggregate_get_id_names(id_type: str) -> Optional[base.dict_keys]:
    giif = get_giif()
    if giif is None:
        return None
    giif2 = giif.get(id_type)
    if giif2 is None:
        return None
    return giif2.keys()


def aggregate_get_gem_by_id(id_type: str, id_name: str) -> Optional[dict]:
    giif = get_giif()
    if giif is None:
        return None
    giif2 = giif.get(id_type)
    if giif2 is None:
        return None
    return giif2.get(id_name)


def get_cluster_name(cluster: Optional[base.Cluster]) -> Optional[str]:
    return gem_get_id_name(cluster, "#cluster_name")


def aggregate_get_cluster_names() -> Optional[base.dict_keys]:
    return aggregate_get_id_names("#cluster_name")


def get_cluster_by_cluster_name(cluster_name: str) -> Optional[dict]:
    return aggregate_get_gem_by_id("#cluster_name", cluster_name)
