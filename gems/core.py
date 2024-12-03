from gems.facets import gems_query, local_ids_update, local_tags_update, attrs_update


def build_indexes(cluster: dict) -> None:
    for gem in gems_query.get_gems(cluster):
        local_ids_update.build_index(gem)
        local_tags_update.build_index(gem)


def create_gem(cluster: dict, gem_parent: dict, gem_base_name: str) -> dict | None:
    gem = {}
    attrs_update.set_cluster(gem, cluster)
    attrs_update.set_gem_parent(gem, gem_parent)
    local_ids_update.set_gem_base_name(cluster, gem_base_name)
    return gem
