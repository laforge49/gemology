from pdml import saver


dict_keys = type({}.keys())


def get_af(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    return gem.get("AttrsFacet")


def get_attr_names(gem: dict | None) -> dict_keys | None:
    af = get_af(gem)
    if af is None:
        return None
    return af.keys()


def get_attr_value(gem: dict | None, attr_name: str) -> any:
    af = get_af(gem)
    if af is None:
        return None
    return af.get(attr_name)


def make_af(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    af = get_af(gem)
    if af is None:
        af = {}
        gem["AttrsFacet"] = af
    return af


def set_attr_value(gem: dict | None, attr_name: str, attr_value: any) -> None:
    af = make_af(gem)
    if af is None:
        return None
    af[attr_name] = attr_value


def get_cluster(gem: dict | None) -> dict | None:
    return get_attr_value(gem, "#cluster")


def set_cluster(gem: dict | None, cluster: dict) -> None:
    set_attr_value(gem, "#cluster", cluster)


def get_cluster_path(gem: dict | None) -> str | None:
    return get_attr_value(gem, "#cluster_path")


def set_cluster_path(gem: dict | None, cluster_path: str) -> None:
    set_attr_value(gem, "#cluster_path", cluster_path)

def get_gem_parent(gem: dict | None) -> dict | None:
    return get_attr_value(gem, "#gem_parent")


def set_gem_parent(gem: dict | None, gem_parent: dict) -> None:
    set_attr_value(gem, "#gem_parent", gem_parent)


def test():
    print()
    print("*** attrs test ***")
    print()
    gem = {}
    cluster = {}
    set_cluster(gem, cluster)
    set_cluster_path(cluster, "fudge")
    print(gem)
    print()
    print("cluster:")
    saver.debug(cluster)
    print()
    print("gem:")
    saver.debug(gem)


if __name__ == "__main__":
    test()
