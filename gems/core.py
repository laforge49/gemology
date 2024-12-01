from gems.facets import gems_facet, local_ids_facet, local_tags_facet


def build_indexes(cluster: dict)-> None:
    for gem in gems_facet.get_gems(cluster):
        local_ids_facet.build_index(gem)
        local_tags_facet.build_index(gem)