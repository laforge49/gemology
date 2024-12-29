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
