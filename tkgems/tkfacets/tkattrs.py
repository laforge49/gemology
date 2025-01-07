from typing import *

from gems import base
from gems.facets import attrs_update, attrs_query


def get_columns(tkgem: Optional[base.Gem]) -> Optional[list]:
    return attrs_query.get_attr_value(tkgem, "columns")


def get_events(tkgem: Optional[base.Gem]) -> Optional[dict]:
     return attrs_query.get_attr_value(tkgem, "events")


def get_geometry(tkgem: Optional[base.Gem]) -> Optional[str]:
    return attrs_query.get_attr_value(tkgem, "geometry")


def get_grid(tkgem: Optional[base.Gem]) -> Optional[dict]:
     return attrs_query.get_attr_value(tkgem, "grid")


def get_is_widget(tkdescriptor_gem: Optional[base.Gem]) -> Optional[bool]:
    return attrs_query.get_attr_value(tkdescriptor_gem, "is_widget")


def set_is_widget(tkdescriptor_gem: Optional[base.Gem], is_widget: bool) -> bool:
    return attrs_update.set_attr_value(tkdescriptor_gem, "is_widget", is_widget)


def get_manual(tkgem: Optional[base.Gem]) -> Optional[bool]:
    return attrs_query.get_attr_value(tkgem, "manual")


def get_options(tkgem: Optional[base.Gem]) -> Optional[dict]:
     return attrs_query.get_attr_value(tkgem, "options")


def get_pack(tkgem: Optional[base.Gem]) -> Optional[dict]:
     return attrs_query.get_attr_value(tkgem, "pack")


def get_packable(tkdescriptor_gem: Optional[base.Gem]) -> Optional[bool]:
    return attrs_query.get_attr_value(tkdescriptor_gem, "packable")


def set_packable(tkdescriptor_gem: Optional[base.Gem], packable: bool) -> bool:
    return attrs_update.set_attr_value(tkdescriptor_gem, "packable", packable)


def get_rows(tkgem: Optional[base.Gem]) -> Optional[list]:
    return attrs_query.get_attr_value(tkgem, "rows")


def get_title(tkgem: Optional[base.Gem]) -> Optional[str]:
    return attrs_query.get_attr_value(tkgem, "title")


def get_tkheight(tkgem: Optional[base.Gem]) -> Optional[int]:
    return attrs_query.get_attr_value(tkgem, "height")


def get_tkobject(tkgem: Optional[base.Gem]) -> any:
    tkobject = attrs_query.get_attr_value(tkgem, "#tkobject")
    return tkobject


def set_tkobject(tkgem: Optional[base.Gem], tkobject: any) -> bool:
    return attrs_update.set_attr_value(tkgem, "#tkobject", tkobject)


def get_tkwidth(tkgem: Optional[base.Gem]) -> Optional[int]:
    return attrs_query.get_attr_value(tkgem, "width")


def get_view_gem(tkgem: Optional[base.Gem]) -> Optional[base.Gem]:
    return attrs_query.get_attr_value(tkgem, "#view_gem")


def set_view_gem(tkgem: Optional[base.Gem], view_gem: Optional[base.Gem]) -> bool:
    return attrs_update.set_attr_value(tkgem, "#view_gem", view_gem)
