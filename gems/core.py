from gems.facets import gems_query, local_ids_update, local_tags_update


def build_indexes(cluster: dict) -> None:
    for gem in gems_query.get_gems(cluster):
        local_ids_update.build_index(gem)
        local_tags_update.build_index(gem)
