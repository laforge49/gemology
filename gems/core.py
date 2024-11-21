from pdml import saver, loader
import pathlib
import copy


aggregate_ = None


def get_facet_attrs(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    return gem.get("AttrsFacet")


def make_facet_attrs(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    attrs_facet = get_facet_attrs(gem)
    if attrs_facet is None:
        attrs_facet = {}
        gem["AttrsFacet"] = attrs_facet
    return attrs_facet


def get_attr(gem: dict | None, attr_name: str) -> any:
    attr_facet = get_facet_attrs(gem)
    if attr_facet is None:
        return None
    return attr_facet.get(attr_name)


def get_attr_cluster(gem: dict | None) -> dict | None:
    return get_attr(gem, "#cluster")


def get_attr_cluster_path(gem: dict | None) -> str | None:
    return get_attr(gem, "#cluster_path")


def get_attr_gem_parent(gem: dict | None) -> dict | None:
    return get_attr(gem, "#gem_parent")


def get_facet_cluster_tags(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    return gem.get("ClusterTagsFacet")


def make_facet_cluster_tags(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    cluster_tags_facet = get_facet_cluster_tags(gem)
    if cluster_tags_facet is None:
        cluster_tags_facet = {}
        gem["ClusterTagsFacet"] = cluster_tags_facet
    return cluster_tags_facet


def get_cluster_tag(gem: dict | None, tag_name: str) -> any:
    cluster_tags_facet = get_facet_cluster_tags(gem)
    if cluster_tags_facet is None:
        return None
    return cluster_tags_facet.get(tag_name)


def get_cluster_tag_gem_base_name(gem: dict | None) -> str | None:
    return get_cluster_tag(gem, "gem_base_name")


def get_cluster_tag_facet_names(gem: dict | None) -> list | None:
    return get_cluster_tag(gem, "#facet_names")


def get_facet_aggregate_tags(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    return gem.get("AggregateTagsFacet")


def make_facet_aggregate_tags(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    aggregate_tags_facet = get_facet_aggregate_tags(gem)
    if aggregate_tags_facet is None:
        aggregate_tags_facet = {}
        gem["AggregateTagsFacet"] = aggregate_tags_facet
    return aggregate_tags_facet


def get_aggregate_tag(gem: dict | None, tag_name: str) -> any:
    aggregate_tags_facet = get_facet_aggregate_tags(gem)
    if aggregate_tags_facet is None:
        return None
    return aggregate_tags_facet.get(tag_name)


def get_aggregate_tag_cluster_name(gem: dict | None) -> str | None:
    return get_aggregate_tag(gem, "#cluster_name")


def get_facet_inverted_cluster_tags(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    return gem.get("#InvertedClusterTagsFacet")


def make_facet_inverted_cluster_tags(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    inverted_cluster_tags_facet = get_facet_inverted_cluster_tags(gem)
    if inverted_cluster_tags_facet is None:
        inverted_cluster_tags_facet = {}
        gem["#InvertedClusterTagsFacet"] = inverted_cluster_tags_facet
    return inverted_cluster_tags_facet


def get_facet_inverted_aggregate_tags(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    return gem.get("#InvertedAggregateTagsFacet")


def make_facet_inverted_aggregate_tags(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    inverted_aggregate_tags_facet = get_facet_inverted_aggregate_tags(gem)
    if inverted_aggregate_tags_facet is None:
        inverted_aggregate_tags_facet = {}
        gem["#InvertedAggregateTagsFacet"] = inverted_aggregate_tags_facet
    return inverted_aggregate_tags_facet


def get_gems_facet(gem: dict | None ) -> list | None:
    if gem is None:
        return None
    return gem.get("GemsFacet")


def make_facet_gems(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    gems_facet = get_gems_facet(gem)
    if gems_facet is None:
        gems_facet = {}
        gem["GemsFacet"] = gems_facet
    return gems_facet


def get_aggregate() -> dict:
    global aggregate_
    if aggregate_:
        return aggregate_
    aggregate_ = {}
    register_(aggregate_, aggregate_)
    return aggregate_


def register_(gem: dict, cluster: dict) -> None:
    pass
