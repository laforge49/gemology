class Gem(dict):
    pass


class Cluster(Gem):
    pass


class Aggregate(Cluster):
    pass


class_map = {"base.Gem": Gem, "base.Cluster": Cluster, "base.Aggregate": Aggregate}
dict_keys = type({}.keys())
aggregate_: Aggregate | None = None


def get_aggregate() -> Aggregate | None:
    global aggregate_
    return aggregate_

def set_aggregate(aggregate: Aggregate) -> None:
    global aggregate_
    aggregate_ = aggregate


def idindex(lst: list, e: any) -> int | None:
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
