from typing import *

from gems import base
from gems.facets import global_tags_query


def get_init_tkgem(tkgem: Optional[base.Gem]) -> any:
    return global_tags_query.gem_get_tag_value(tkgem, "init_tkgem")


def get_scrolling_name(tkgem: Optional[base.Gem]) -> any:
    return global_tags_query.gem_get_tag_value(tkgem, "ScrollingName")


def get_tktype(tkgem: Optional[base.Gem]) -> any:
    return global_tags_query.gem_get_tag_value(tkgem, "TkType")
