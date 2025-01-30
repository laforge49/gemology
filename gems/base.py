from typing import *


def findin(col: list | str, v: str) -> int | None:
    if v in col:
        return col.index(v)
    return None


def isscalar(x: any) -> bool:
    return isinstance(x, (int, float, complex, str, bytes, bool))


scalar = int | float | complex | str | bytes | bool


class GemBaseName(str):
    pass


class GemName(str):
    pass


class ClusterName(str):
    pass


class FullGemName(GemName):
    pass


def full_gem_name_to_cluster_name(name: FullGemName) -> Optional[ClusterName]:
    if name is None:
        return None
    i = findin(name, ".")
    if i is None:
        assert isinstance(name, ClusterName)
        return name
    cluster_name = name[:i]
    assert isinstance(cluster_name, ClusterName)
    return cluster_name


def expand_gem_name(name: GemName, context: FullGemName) -> Optional[FullGemName]:
    if name is None:
        return None
    i = findin(name, ".")
    if i == 1:
        cluster_name = full_gem_name_to_cluster_name(context)
        full_gem_name = cluster_name + name
        assert isinstance(full_gem_name, FullGemName)
        return full_gem_name
    assert isinstance(name, FullGemName)
    return name



class Gem(Dict[str, dict | list]):
    pass


class Cluster(Gem):
    pass


class Aggregate(Cluster):
    pass


class Resources(Gem):
    pass


class ResourceGroup(Gem):
    pass


class Resource(Gem):
    pass


class AttrsFacet(Dict[str, scalar]):
    pass


class GemsFacet(List[Gem]):
    pass


class GlobalIdsFacet(Dict[str, scalar]):
    pass


class GlobalIdIndexFacet(Dict[str, Dict[str, Gem]]):
    pass


class GlobalTagsFacet(Dict[str, scalar]):
    pass


class GlobalTagIndexFacet(Dict[str, Dict[scalar, List[Gem]]]):
    pass


class LocalIdsFacet(Dict[str, str]):
    pass


class LocalIdIndexFacet(Dict[str, Dict[str, Gem]]):
    pass


class LocalTagsFacet(Dict[str, scalar]):
    pass


class LocalTagIndexFacet(Dict[str, Dict[scalar, List[Gem]]]):
    pass


class_map = {"base.Gem": Gem,
             "base.Cluster": Cluster,
             "base.Aggregate": Aggregate,
             "base.Resources": Resources,
             "base.ResourceGroup": ResourceGroup,
             "base.Resource": Resource}
dict_keys = type({}.keys())
aggregate_: Optional[Aggregate] = None


def get_aggregate() -> Optional[Aggregate]:
    global aggregate_
    return aggregate_


def set_aggregate(aggregate: Aggregate) -> None:
    global aggregate_
    aggregate_ = aggregate


def idindex(lst: list, e: any) -> Optional[int]:
    ndx = 0
    for x in lst:
        if x is e:
            return ndx
        ndx += 1
    return None


def idremove(lst: list, e: any) -> bool:
    ndx = idindex(lst, e)
    if ndx is None:
        return False
    del lst[ndx]
    return True
