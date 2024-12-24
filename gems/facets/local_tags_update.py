from typing import *


from gems import base
from gems.facets import attrs_query, local_tags_query


def make_ltf(gem: Optional[base.Gem]) -> Optional[base.LocalTagsFacets]:
    if gem is None:
        return None
    ltf = local_tags_query.get_ltf(gem)
    if ltf is None:
        ltf = base.LocalTagsFacets()
        gem["LocalTagsFacet"] = ltf
    assert isinstance(ltf, base.LocalTagsFacets)
    return ltf


def deindex_tag(gem: Optional[base.Gem], tag_name: str, tag_value: str) -> bool:
    if gem is None:
        return False
    cluster = attrs_query.get_cluster(gem)
    if cluster is None:
        return None
    ltif = local_tags_query.cluster_get_ltif(cluster)
    if ltif is None:
        return False
    ltif2 = ltif.get(tag_name)
    if ltif2 is None:
        return False
    gems = ltif2.get(tag_value)
    if gems is None:
        return False
    return base.idremove(gems, gem)


def del_tag(gem: Optional[base.Gem], tag_name: str) -> bool:
    if gem is None:
        return False
    ltf = local_tags_query.get_ltf(gem)
    if ltf is None:
        return False
    tag_value = ltf.get(tag_name)
    if tag_value is None:
        return False
    del ltf[tag_name]
    deindex_tag(gem, tag_name, tag_value)
    return True


def cluster_make_ltif(cluster: Optional[base.Cluster]) -> Optional[dict]:
    ltif = local_tags_query.cluster_get_ltif(cluster)
    if ltif is None:
        ltif = {}
        cluster["#LocalTagIndexFacet"] = ltif
    return ltif


def cluster_make_ltif2(cluster: Optional[base.Cluster], tag_name: str) -> Optional[dict]:
    ltif = cluster_make_ltif(cluster)
    if ltif is None:
        return
    ltif2 = ltif.get(tag_name)
    if ltif2 is None:
        ltif2 = {}
        ltif[tag_name] = ltif2
    return ltif2


def set_tag(gem: Optional[base.Gem], tag_name: str, tag_value: str) -> bool:
    if gem is None:
        return False
    ltf = make_ltf(gem)
    if ltf is None:
        return False
    value = ltf.get(tag_name)
    if value == tag_value:
        return False
    ltf[tag_name] = value
    cluster = attrs_query.get_cluster(gem)
    if cluster is None:
        return False
    ltif2 = cluster_make_ltif2(cluster, tag_name)
    if ltif2 is None:
        return False
    gems = ltif2.get(tag_value)
    if gems:
        gems.remove(gem)
    if gems is None:
        gems = []
        ltif2[tag_value] = gems
    gems.append(gem)
    return True


def build_index(gem: Optional[base.Gem]) -> bool:
    ltf = local_tags_query.get_ltf(gem)
    if ltf is None:
        return False
    cluster = attrs_query.get_cluster(gem)
    if cluster is None:
        return False
    tag_names = ltf.keys()
    for tag_name in tag_names:
        tag_value = ltf.get(tag_name)
        if tag_value is not None:
            ltif2 = cluster_make_ltif2(cluster, tag_name)
            if ltif2 is None:
                return False
            gems = ltif2.get(tag_value)
            if gems is None:
                gems = []
                ltif2[tag_value] = gems
            if base.idindex(gems, gem) is None:
                gems.append(gem)
    return True
