dict_keys = type({}.keys())


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
