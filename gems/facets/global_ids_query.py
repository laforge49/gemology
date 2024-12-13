from gems import base
from gems.facets import attrs_query


def get_gif(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    return gem.get("GlobalIdsFacet")


def gem_get_id_types(gem: dict | None) -> base.dict_keys | None:
    gif = get_gif(gem)
    if gif is None:
        return None
    return gif.keys()


def gem_get_id_name(gem: dict | None, id_type: str) -> str | None:
    gif = get_gif(gem)
    if gif is None:
        return None
    return gif.get(id_type)


def get_giif() -> dict | None:
    aggregate = base.get_aggregate()
    return aggregate.get("#GlobalIdIndexFacet")


def aggregate_get_id_types() -> base.dict_keys | None:
    giif = get_giif()
    if giif is None:
        return None
    return giif.keys()


def aggregate_get_id_names(id_type: str) -> base.dict_keys | None:
    giif = get_giif()
    if giif is None:
        return None
    giif2 = giif.get(id_type)
    if giif2 is None:
        return None
    return giif2.keys()


def aggregate_get_gem_by_id(id_type: str, id_name: str) -> dict | None:
    giif = get_giif()
    if giif is None:
        return None
    giif2 = giif.get(id_type)
    if giif2 is None:
        return None
    return giif2.get(id_name)


def get_cluster_name(cluster: dict | None) -> str | None:
    return gem_get_id_name(cluster, "#cluster_name")


def aggregate_get_cluster_names() -> base.dict_keys | None:
    return aggregate_get_id_names("#cluster_name")


def get_cluster_by_cluster_name(cluster_name: str) -> dict | None:
    return aggregate_get_gem_by_id("#cluster_name", cluster_name)
