dict_keys = type({}.keys())
aggregate_ = None


def get_aggregate() -> dict:
    global aggregate_
    if aggregate_:
        return aggregate_
    aggregate_ = {}
    return aggregate_


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
