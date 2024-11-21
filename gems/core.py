aggregate_ = None


def make_aggregate() -> dict:
    global aggregate_
    if aggregate_:
        return aggregate_
    aggregate_ = {}
    register_(aggregate_, aggregate_)
    return aggregate_


def register_(gem: dict, cluster: dict) -> None:
    pass
