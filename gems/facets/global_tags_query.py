from typing import *


from gems import base
from gems.facets import attrs_query, global_ids_query, local_ids_query


def get_gtf(gem: Optional[base.Gem]) -> Optional[base.GlobalTagsFacet]:
    if gem is None:
        return None
    facet = gem.get("GlobalTagsFacet")
    assert isinstance(facet, base.GlobalTagsFacet) or facet is None
    return facet


def gem_get_tag_names(gem: Optional[base.Gem]) -> Optional[base.dict_keys]:
    gtf = get_gtf(gem)
    if gtf is None:
        return None
    return gtf.keys()


def gem_get_tag_value(gem: Optional[base.Gem], tag_name: str) -> Optional[base.scalar]:
    gtf = get_gtf(gem)
    if gtf is None:
        return None
    return gtf.get(tag_name)


def expand_gem_name(source_gem: base.Gem, gemname: str) -> Optional[str]:
    if gemname is None:
        return None
    if gemname.startswith("."):
        cluster = attrs_query.get_cluster(source_gem)
        if cluster is None:
            cluster = source_gem
        if isinstance(cluster, base.Aggregate):
            cluster_name = "Aggregate"
        elif gemname == ".":
            cluster_name = global_ids_query.get_cluster_name(cluster)
            return cluster_name
        else:
            cluster_name = global_ids_query.get_cluster_name(cluster)
            if cluster_name is None:
                return None
        return cluster_name + gemname
    else:
        return gemname


def gem_get_full_gem_name(source_gem: Optional[base.Gem], tag_name: str) -> Optional[str]:
    if source_gem is None:
        return None
    gemname = gem_get_tag_value(source_gem, tag_name)
    return expand_gem_name(source_gem, gemname)


def resolve_link(source_gem: base.Gem, tag_name: str) -> Optional[base.Gem]:
    full_gemname = gem_get_full_gem_name(source_gem, tag_name)
    if full_gemname is None:
        return None
    if full_gemname == "Aggregate":
        gem_basename = None
        cluster = global_ids_query.get_cluster_by_cluster_name(full_gemname)
    elif "." not in full_gemname:
        gem_basename = None
        cluster = global_ids_query.get_cluster_by_cluster_name(full_gemname)
    else:
        cluster_name, gem_basename = full_gemname.split(".")
        cluster = global_ids_query.get_cluster_by_cluster_name(cluster_name)
    if cluster is None:
        return None
    if gem_basename is None:
        return cluster
    gem = local_ids_query.cluster_get_gem_by_gem_base_name(cluster, gem_basename)
    return gem


def get_gtif() -> Optional[base.GlobalTagIndexFacet]:
    aggregate = base.get_aggregate()
    gtif = aggregate.get("#GlobalTagIndexFacet")
    assert isinstance(gtif, base.GlobalTagIndexFacet) or gtif is None
    return gtif


def aggregate_get_tag_names() -> Optional[base.dict_keys]:
    gtif = get_gtif()
    if gtif is None:
        return None
    return gtif.keys()


def aggregate_get_tag_values(tag_name: str) -> Optional[base.dict_keys]:
    gtif = get_gtif()
    if gtif is None:
        return None
    gtif2 = gtif.get(tag_name)
    if gtif2 is None:
        return None
    return gtif2.keys()


def aggregate_get_gems_by_tag(tag_name: str, tag_value: str) -> Optional[list]:
    gtif = get_gtif()
    if gtif is None:
        return None
    gtif2 = gtif.get(tag_name)
    if gtif2 is None:
        return None
    return gtif2.get(tag_value)


def get_description(gem: Optional[base.Gem]) -> Optional[any]:
    return gem_get_tag_value(gem, "description")


def aggregate_get_descriptions() -> Optional[base.dict_keys]:
    return aggregate_get_tag_values("description")


def get_gems_by_description(description: str) -> Optional[list]:
    return aggregate_get_gems_by_tag("description", description)
