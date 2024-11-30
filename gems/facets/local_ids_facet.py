from gems.facets import gems_facet, attrs_facet


def get_lif(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    return gem.get("LocalIdsFacet")


def get_id_types(gem: dict | None) -> gems_facet.dict_keys | None:
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


def get_liif(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    cluster = attrs_facet.get_cluster(gem)
    return cluster.get("#LocalIdIndexFacet")


def get_index_id_types(gem: dict | None) -> gems_facet.dict_keys | None:
    liif = get_liif(gem)
    if liif is None:
        return None
    return liif.keys()


def get_index_id_names(gem: dict | None, id_type: str) -> gems_facet.dict_keys | None:
    liif = get_liif(gem)
    if liif is None:
        return None
    liif2 = liif.get(id_type)
    if liif2 is None:
        return None
    return liif2.keys()


def get_gem_by_id(gem: dict | None, id_type: str, id_name: str) -> dict | None:
    liif = get_liif(gem)
    if liif is None:
        return None
    liif2 = liif.get(id_type)
    if liif2 is None:
        return None
    return liif2.get(id_name)


def del_id(gem: dict | None, id_type: str, id_name: str) -> None:
    cluster = attrs_facet.get_cluster(gem)
    gem = get_gem_by_id(cluster, id_type, id_name)
    if gem is None:
        return
    lif = get_lif(gem)
    del lif[id_type]
    liif = get_liif(gem)
    liif2 = liif.get(id_type)
    del liif2[id_name]


def make_liif(gem: dict | None) -> dict | None:
    cluster = attrs_facet.get_cluster(gem)
    if cluster is None:
        return None
    liif = get_liif(cluster)
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


def set_id(gem: dict | None, id_type: str, id_name: str) -> None:
    cluster = attrs_facet.get_cluster(gem)
    if cluster is None:
        return
    del_id(cluster, id_type, id_name)
    lif = make_lif(gem)
    lif[id_type] = id_name
    liif2 = make_liif2(cluster, id_type)
    liif2[id_name] = gem


def get_gem_base_name(gem: dict | None) -> str | None:
    return get_id_name(gem, "gem_base_name")


def get_gem_by_gem_base_name(gem: dict | None, gem_base_name: str) -> dict | None:
    return get_gem_by_id(gem, "gem_base_name", gem_base_name)


def del_gem_base_name(gem: dict | None, id_type: str, id_name: str) -> None:
    del_id(gem, id_type, id_name)


def set_gem_base_name(gem: dict | None, gem_base_name: str) -> None:
    set_id(gem, "gem_base_name", gem_base_name)
