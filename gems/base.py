from typing import *


class AttrsFacet(dict):
    pass

class GemsFacet(list):
    pass


class GlobalIdsFacet(dict):
    pass


class GlobalIdIndexFacet(dict):
    pass


class GlobalTagsFacet(dict):
    pass


class GlobalTagIndexFacet(dict):
    pass


class LocalIdsFacet(dict):
    pass


class LocalIdIndexFacet(dict):
    pass


class LocalTagsFacet(dict):
    pass


class LocalTagIndexFacet(dict):
    pass


class Gem(dict):
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
