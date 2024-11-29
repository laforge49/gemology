dict_keys = type({}.keys())



def get_af(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    return gem.get("AttrsFacet")


def get_names(gem: dict | None) -> dict_keys | None:
    if gem is None:
        return None
    return gem.keys()


def get_value(gem: dict | None, name: str) -> any:
    af = get_af(gem)
    if af is None:
        return None
    return af.get(name)


def make_af(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    af = get_af(gem)
    if af is None:
        af = {}
        gem["AttrsFacet"] = af
    return af


def get_cluster(gem: dict | None) -> dict | None:
    return get_value(gem, "#cluster")


def set_cluster(gem: dict | None, cluster: dict) -> None:
    af = make_af(gem)
    if af is None:
        return None
    af["#cluster"] = cluster


def get_cluster_path(gem: dict | None) -> str | None:
    return get_value(gem, "#cluster_path")


def set_cluster_path(gem: dict | None, cluster_path: str) -> None:
    af = make_af(gem)
    if af is None:
        return None
    af["#cluster_path"] = cluster_path


def get_gem_parent(gem: dict | None) -> dict | None:
    return get_value(gem, "#gem_parent")


def set_gem_parent(gem: dict | None, gem_parent: dict) -> None:
    af = make_af(gem)
    if af is None:
        return None
    af["#gem_parent"] = gem_parent
