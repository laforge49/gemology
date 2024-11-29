from gems.facets import attrs

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


def get_gem_by_id(cluster: dict | None, id_type: str, id_name: str) -> dict | None:
    liif = get_liif(cluster)
    if liif is None:
        return None
    liif2 = liif.get(id_type)
    if liif2 is None:
        return None
    return liif2.get(id_name)


def del_id(cluster: dict | None, id_type: str, id_name: str) -> None:
    gem = get_gem_by_id(cluster, id_type, id_name)
    if gem is None:
        return
    lif = get_lif(gem)
    del lif[id_type]
    liif = get_liif(cluster)
    liif2 = liif.get(id_type)
    del liif2[id_name]


def make_liif(cluster: dict | None) -> dict | None:
    if cluster is None:
        return None
    liif = get_liif(cluster)
    if liif is None:
        liif = {}
        cluster["#LocalIdIndexFacet"] = liif
    return liif


def make_liif2(cluster: dict | None, id_type: str) -> dict | None:
    liif = make_liif(cluster)
    if liif is None:
        return
    liif2 = liif.get(id_type)
    if liif2 is None:
        liif2 = {}
        liif[id_type] = liif2
    return liif2


def set_id(gem: dict | None, id_type: str, id_name: str) -> None:
    cluster = attrs.get_cluster(gem)
    if cluster is None:
        return
    del_id(cluster, id_type, id_name)
    lif = make_lif(gem)
    lif[id_type] = id_name
    liif2 = make_liif2(cluster, id_type)
    liif2[id_name] = gem


def get_gem_base_name(gem: dict | None) -> str | None:
    return get_id_name(gem, "gem_base_name")


def get_gem_by_gem_base_name(cluster: dict | None, gem_base_name: str) -> dict | None:
    return get_gem_by_id(cluster, "gem_base_name", gem_base_name)


def del_gem_base_name(cluster: dict | None, id_type: str, id_name: str) -> None:
    del_id(cluster, id_type, id_name)


def set_gem_base_name(gem: dict | None, gem_base_name: str) -> None:
    set_id(gem, "gem_base_name", gem_base_name)
