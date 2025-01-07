from typing import *


from gems import base


def get_gif(gem: Optional[base.Gem]) -> Optional[base.GlobalIdsFacet]:
    if gem is None:
        return None
    facet = gem.get("GlobalIdsFacet")
    assert isinstance(facet, base.GlobalIdsFacet) or facet is None
    return facet


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


def get_giif() -> Optional[base.GlobalIdIndexFacet]:
    aggregate = base.get_aggregate()
    facet = aggregate.get("#GlobalIdIndexFacet")
    assert isinstance(facet, base.GlobalIdIndexFacet) or facet is None
    return facet


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


def aggregate_get_gem_by_id(id_type: str, id_name: str) -> Optional[base.Gem]:
    giif = get_giif()
    if giif is None:
        return None
    giif2 = giif.get(id_type)
    if giif2 is None:
        return None
    gem = giif2.get(id_name)
    assert isinstance(gem, base.Gem) or gem is None
    return gem


def get_cluster_name(cluster: Optional[base.Cluster]) -> Optional[str]:
    return gem_get_id_name(cluster, "#cluster_name")


def aggregate_get_cluster_names() -> Optional[base.dict_keys]:
    return aggregate_get_id_names("#cluster_name")


def get_cluster_by_cluster_name(cluster_name: str) -> Optional[base.Cluster]:
    if cluster_name == "Aggregate":
        return base.get_aggregate()
    cluster = aggregate_get_gem_by_id("#cluster_name", cluster_name)
    assert isinstance(cluster, base.Cluster) or cluster is None
    return cluster
