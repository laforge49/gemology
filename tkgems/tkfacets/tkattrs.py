import typing

from gems.facets import attrs_update, attrs_query


def get_is_widget(tkdescriptor_gem: dict | None) -> bool | None:
    return attrs_query.get_attr_value(tkdescriptor_gem, "is_widget")


def set_is_widget(tkdescriptor_gem: dict | None, is_widget: bool) -> bool:
    return attrs_update.set_attr_value(tkdescriptor_gem, "is_widget", is_widget)


def get_packable(tkdescriptor_gem: dict | None) -> bool | None:
    return attrs_query.get_attr_value(tkdescriptor_gem, "packable")


def set_packable(tkdescriptor_gem: dict | None, packable: bool) -> bool:
    return attrs_update.set_attr_value(tkdescriptor_gem, "packable", packable)


def get_tkcomposer(tkdescriptor_gem: dict | None) -> typing.Callable | None:
    return attrs_query.get_attr_value(tkdescriptor_gem, "#tkcomposer")


def set_tkcomposer(tkdescriptor_gem: dict | None, tkcomposer: typing.Callable) -> bool:
    return attrs_update.set_attr_value(tkdescriptor_gem, "#tkcomposer", tkcomposer)


def get_tkheight(tkgem: dict | None) -> int | None:
    h = attrs_query.get_attr_value(tkgem, "height")
    if h:
        return int(h)
    return None


def get_tkwidth(tkgem: dict | None) -> int | None:
    w = attrs_query.get_attr_value(tkgem, "width")
    if w:
        return int(w)
    return None
