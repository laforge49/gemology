from typing import *

from gems import base
from gems.facets import global_tags_query


def get_init_tkgem(tkgem: Optional[base.Gem]) -> Optional[str]:
    init_tkgem = global_tags_query.gem_get_tag_value(tkgem, "init_tkgem")
    assert isinstance(init_tkgem, str) or init_tkgem is None
    return init_tkgem


def get_tktype(tkgem: Optional[base.Gem]) -> str:
    tktype = global_tags_query.gem_get_tag_value(tkgem, "TkType")
    assert isinstance(tktype, str)
    return tktype


def get_command(gem: Optional[base.Gem]) -> Optional[any]:
    return global_tags_query.gem_get_tag_value(gem, "command")


def resolve_master_frame(gem: Optional[base.Gem]) -> Optional[any]:
    return global_tags_query.resolve_link(gem, "master_frame")


def resolve_VariableGemName(gem: Optional[base.Gem]) -> Optional[any]:
    return global_tags_query.resolve_link(gem, "VariableGemName")


def resolve_TextVariableGemName(gem: Optional[base.Gem]) -> Optional[any]:
    return global_tags_query.resolve_link(gem, "TextVariableGemName")


def resolve_ListVariableGemName(gem: Optional[base.Gem]) -> Optional[any]:
    return global_tags_query.resolve_link(gem, "ListVariableGemName")


def resolve_ScrollingGemName(gem: Optional[base.Gem]) -> Optional[any]:
    return global_tags_query.resolve_link(gem, "ScrollingGemName")
