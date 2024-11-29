

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


def make_lif(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    lif = get_lif(gem)
    if lif is None:
        lif = {}
        gem["LocalIdsFacet"] = lif
    return lif


def get_gem_base_name(gem: dict | None) -> str | None:
    return get_id_name(gem, "gem_base_name")


def get_liif(cluster: dict | None) -> dict | None:
    if cluster is None:
        return None
    return cluster.get("#LocalIdIndexFacet")


def get_index_id_types(cluster: dict | None) -> dict_keys | None:
    liif = get_liif(cluster)
    if liif is None:
        return None
    return liif.keys()


def get_index_id_names(cluster: dict | None, id_type: str) -> dict_keys | None:
    liif = get_liif(cluster)
    if liif is None:
        return None
    liif2 = liif.get(id_type)
    if liif2 is None:
        return None
    return liif2.keys()


def make_liif(cluster: dict | None) -> dict | None:
    if cluster is None:
        return None
    liif = get_liif(cluster)
    if liif is None:
        liif = {}
        cluster["#LocalIdIndexFacet"] = liif
    return liif


def get_gem_by_id(cluster: dict | None, id_type: str, id_name: str) -> dict | None:
    liif = get_liif(cluster)
    if liif is None:
        return None
    liif2 = liif.get(id_type)
    if liif2 is None:
        return None
    return liif2.get(id_name)


def get_gem_by_gem_base_name(cluster: dict | None, gem_base_name: str) -> dict | None:
    return get_gem_by_id(cluster, "gem_base_name", gem_base_name)
