from pdml import saver, loader
import pathlib
import copy


def get_facet_cluster_tags(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    return gem.get("ClusterTagsFacet")


def get_cluster_tag_values(gem: dict | None, tag_name: str) -> list | None:
    cluster_tags_facet = get_facet_cluster_tags(gem)
    if cluster_tags_facet is None:
        return None
    return cluster_tags_facet.get(tag_name)


def get_cluster_tag_facet_names(gem: dict | None) -> list | None:
    return get_cluster_tag_values(gem, "#facet_names")


def make_facet_cluster_tags(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    cluster_tags_facet = get_facet_cluster_tags(gem)
    if cluster_tags_facet is None:
        cluster_tags_facet = {}
        gem["ClusterTagsFacet"] = cluster_tags_facet
    return cluster_tags_facet


def get_facet_inverted_cluster_tags(cluster: dict | None) -> dict | None:
    if cluster is None:
        return None
    return cluster.get("#InvertedClusterTagsFacet")


def make_facet_inverted_cluster_tags(cluster: dict | None) -> dict | None:
    if cluster is None:
        return None
    inverted_cluster_tags_facet = get_facet_inverted_cluster_tags(cluster)
    if inverted_cluster_tags_facet is None:
        inverted_cluster_tags_facet = {}
        cluster["#InvertedClusterTagsFacet"] = inverted_cluster_tags_facet
    return inverted_cluster_tags_facet


def get_facet_aggregate_ids(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    return gem.get("AggregateIdsFacet")


def get_aggregate_id_name(gem: dict | None, id_type: str) -> str | None:
    aggregate_ids_facet = get_facet_aggregate_ids(gem)
    if aggregate_ids_facet is None:
        return None
    return aggregate_ids_facet.get(id_type)


def get_aggregate_id_cluster_name(cluster: dict | None) -> str | None:
    return get_aggregate_id_name(cluster, "#cluster_name")


def make_facet_aggregate_ids(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    aggregate_ids_facet = get_facet_aggregate_ids(gem)
    if aggregate_ids_facet is None:
        aggregate_ids_facet = {}
        gem["AggregateTagsFacet"] = aggregate_ids_facet
    return aggregate_ids_facet


def get_facet_inverted_aggregate_ids(aggregate: dict | None) -> dict | None:
    if aggregate is None:
        return None
    return aggregate.get("#InvertedAggregateIdsFacet")


def get_inverted_aggregate_ids(aggregate: dict | None, id_type: str) -> dict | None:
    inverted_aggregate_ids_facet = get_facet_inverted_cluster_ids(aggregate)
    if inverted_aggregate_ids_facet is None:
        return None
    return inverted_aggregate_ids_facet.get(id_type)


def get_inverted_aggregate_id(aggregate: dict | None, id_type: str, id: str) -> dict | None:
    inverted_aggregate_id = get_inverted_aggregate_ids(aggregate, id_type)
    if inverted_aggregate_id is None:
        return None
    return inverted_aggregate_id.get(id)


def get_cluster_by_name(aggregate: dict | None, gem_base_name: str) -> dict | None:
    return get_inverted_aggregate_id(aggregate, "#cluster_nam", gem_base_name)


def make_facet_inverted_aggregate_ids(aggregate: dict | None) -> dict | None:
    if aggregate is None:
        return None
    inverted_aggregate_ids_facet = get_facet_inverted_aggregate_ids(aggregate)
    if inverted_aggregate_ids_facet is None:
        inverted_aggregate_ids_facet = {}
        aggregate["#InvertedAggregateIdsFacet"] = inverted_aggregate_ids_facet
    return inverted_aggregate_ids_facet


def get_facet_aggregate_tags(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    return gem.get("AggregateTagsFacet")


def get_aggregate_tag_values(gem: dict | None, tag_name: str) -> list | None:
    aggregate_tags_facet = get_facet_aggregate_tags(gem)
    if aggregate_tags_facet is None:
        return None
    return aggregate_tags_facet.get(tag_name)


def make_facet_aggregate_tags(gem: dict | None) -> dict | None:
    if gem is None:
        return None
    aggregate_tags_facet = get_facet_aggregate_tags(gem)
    if aggregate_tags_facet is None:
        aggregate_tags_facet = {}
        gem["AggregateTagsFacet"] = aggregate_tags_facet
    return aggregate_tags_facet


def get_facet_inverted_aggregate_tags(aggregate: dict | None) -> dict | None:
    if aggregate is None:
        return None
    return aggregate.get("#InvertedAggregateTagsFacet")


def make_facet_inverted_aggregate_tags(aggregate: dict | None) -> dict | None:
    if aggregate is None:
        return None
    inverted_aggregate_tags_facet = get_facet_aggregate_tags(aggregate)
    if inverted_aggregate_tags_facet is None:
        inverted_aggregate_tags_facet = {}
        aggregate["#InvertedAggregateTagsFacet"] = inverted_aggregate_tags_facet
    return inverted_aggregate_tags_facet


aggregate_ = None


def get_aggregate() -> dict:
    global aggregate_
    if aggregate_:
        return aggregate_
    aggregate_ = {}
    register_(aggregate_, aggregate_)
    return aggregate_


def register_(gem: dict, cluster: dict) -> None:
    pass
