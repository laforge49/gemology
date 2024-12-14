import typing

from gems.facets import attrs_update, attrs_query


def get_columns(tkgem: dict | None) -> int | None:
    return attrs_query.get_attr_value(tkgem, "columns")


def get_geometry(tkdescriptor_gem: dict | None) -> str | None:
    return attrs_query.get_attr_value(tkdescriptor_gem, "geometry")


def get_grid(tkdescriptor_gem: dict | None) -> dict | None:
     return attrs_query.get_attr_value(tkdescriptor_gem, "grid")


def get_is_widget(tkdescriptor_gem: dict | None) -> bool | None:
    return attrs_query.get_attr_value(tkdescriptor_gem, "is_widget")


def set_is_widget(tkdescriptor_gem: dict | None, is_widget: bool) -> bool:
    return attrs_update.set_attr_value(tkdescriptor_gem, "is_widget", is_widget)


def get_manual(tkdescriptor_gem: dict | None) -> bool | None:
    return attrs_query.get_attr_value(tkdescriptor_gem, "manual")


def get_options(tkdescriptor_gem: dict | None) -> dict | None:
     return attrs_query.get_attr_value(tkdescriptor_gem, "options")


def get_pack(tkdescriptor_gem: dict | None) -> dict | None:
     return attrs_query.get_attr_value(tkdescriptor_gem, "pack")


def get_packable(tkdescriptor_gem: dict | None) -> bool | None:
    return attrs_query.get_attr_value(tkdescriptor_gem, "packable")


def set_packable(tkdescriptor_gem: dict | None, packable: bool) -> bool:
    return attrs_update.set_attr_value(tkdescriptor_gem, "packable", packable)


def get_rows(tkgem: dict | None) -> int | None:
    return attrs_query.get_attr_value(tkgem, "rows")


def get_title(tkdescriptor_gem: dict | None) -> str | None:
    return attrs_query.get_attr_value(tkdescriptor_gem, "title")


def get_tkcomposer(tkdescriptor_gem: dict | None) -> typing.Callable | None:
    return attrs_query.get_attr_value(tkdescriptor_gem, "#tkcomposer")


def set_tkcomposer(tkdescriptor_gem: dict | None, tkcomposer: typing.Callable) -> bool:
    return attrs_update.set_attr_value(tkdescriptor_gem, "#tkcomposer", tkcomposer)


def get_tkheight(tkgem: dict | None) -> int | None:
    return attrs_query.get_attr_value(tkgem, "height")


def get_tkobject(tkgem: dict | None) -> any:
    tkobject = attrs_query.get_attr_value(tkgem, "#tkobject")
    if tkobject:
        return tkobject
    return None


def set_tkobject(tkgem: dict | None, tkobject: any) -> bool:
    return attrs_update.set_attr_value(tkgem, "#tkobject", tkobject)


def get_tkwidth(tkgem: dict | None) -> int | None:
    return attrs_query.get_attr_value(tkgem, "width")
