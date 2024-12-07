from gems import base


def get_af(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    return gem.get("AttrsFacet")


def get_attr_names(gem: dict | None) -> base.dict_keys | None:
    af = get_af(gem)
    if af is None:
        return None
    return af.keys()


def get_attr_value(gem: dict | None, attr_name: str) -> any:
    af = get_af(gem)
    if af is None:
        return None
    return af.get(attr_name)


def get_cluster(gem: dict | None) -> dict | None:
    cluster = get_attr_value(gem, "#cluster")
    if cluster is None:
        cluster = gem
    return cluster


def get_cluster_path(gem: dict | None) -> str | None:
    return get_attr_value(gem, "#cluster_path")


def get_gem_parent(gem: dict | None) -> dict | None:
    return get_attr_value(gem, "#gem_parent")


def get_function(gem: dict | None) -> str | None:
    return get_attr_value(gem, "#function")
