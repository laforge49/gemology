from typing import *


def findin(col: list | str, v: str) -> int | None:
    if v in col:
        return col.index(v)
    return None


def isscalar(x: any) -> bool:
    return isinstance(x, (int, float, complex, str, bytes, bool))


scalar = int | float | complex | str | bytes | bool


class GemBaseName(str):
    def __new__(cls, name):
        assert "." not in name
        instance = str.__new__(cls, name)
        assert isinstance(instance, GemBaseName)
        return instance


class GemName(str):
    def __new__(cls, name):
        assert not name.endswith(".")
        instance = super().__new__(cls, name)
        assert isinstance(instance, GemName)
        return instance


class GemFullName(GemName):
    def __new__(cls, name):
        assert not name.startswith(".")
        instance = super().__new__(cls, name)
        assert isinstance(instance, GemFullName)
        return instance


class ClusterName(GemName):
    def __new__(cls, name):
        assert "." not in name
        instance = GemName.__new__(cls, name)
        assert isinstance(instance, ClusterName)
        return instance


def gem_full_name_to_cluster_name(name: GemFullName) -> Optional[ClusterName]:
    if name is None:
        return None
    i = findin(name, ".")
    if i is None:
        return ClusterName(name)
    cluster_name = ClusterName(name[:i])
    return cluster_name


def gem_full_name_to_gem_name(name: GemFullName) -> Optional[GemName]:
    if name is None:
        return None
    i = findin(name, ".")
    if i is None:
        gemname = GemName(name)
    else:
        gemname = GemName(name[i:])
    return gemname


def expand_gem_name(name: GemName, context: GemFullName) -> Optional[GemFullName]:
    if name is None:
        return None
    i = findin(name, ".")
    if i == 0 :
        cluster_name = gem_full_name_to_cluster_name(context)
        return GemFullName(cluster_name + name)
    return GemFullName(name)



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
