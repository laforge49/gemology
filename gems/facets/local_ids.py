

dict_keys = type({}.keys())


def get_lif(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    return gem.get("LocalIdsFacet")


def get_id_types(gem: dict | None) -> dict_keys | None:
    lif = get_lif(gem)
    if lif is None:
        return None
    return lif.keys()


def get_id_name(gem: dict | None, id_type: str) -> str | None:
    lif = get_lif(gem)
    if lif is None:
        return None
    return lif.get(id_type)


def get_gem_base_name(gem: dict | None) -> str | None:
    return get_id_name(gem: dict | None, "gem_base_name")


def get_liif(cluster: dict | None) -> dict | None:
    if cluster is None:
        return None
    return cluster.get("#LocalIdIndexFacet")


def get_local_id_types(cluster: dict | None) -> dict_keys | None:
    liif = get_liif(cluster)
    if liif is None:
        return None
    return liif.keys()


def get_local_id_names(cluster: dict | None, id_type: str) -> dict_keys | None:
    liif = get_liif(cluster)
    if liif is None:
        return None
    liif2 = liif.get(id_type)
    if liif2 is None:
        return None
    return liif2.keys()


def get_gem_by_local_id(cluster: dict | None, id_type: str, id_name: str) -> dict | None:
    liif = get_liif(cluster)
    if liif is None:
        return None
    liif2 = liif.get(id_type)
    if liif2 is None:
        return None
    return liif2.get(id_name)


def get_local_gem_by_gem_base_name(gem: dict | None) -> str | None:
    return get_cluster_id_name(gem, "gem_base_name")
