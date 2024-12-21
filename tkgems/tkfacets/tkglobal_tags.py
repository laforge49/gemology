from gems import base
from gems.facets import global_tags_query


def get_init_tkgem(tkgem: dict | None) -> base.dict_keys | None:
    return global_tags_query.gem_get_tag_values(tkgem, "init_tkgem")


def get_tktype(tkgem: dict | None) -> base.dict_keys | None:
    return global_tags_query.gem_get_tag_values(tkgem, "TkType")
