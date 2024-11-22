# ClusterTagsFacet

A ClusterTagsFacet holds a dict of Tag name/value pairs.
These are indexed in the #InvertedClusterTagsFacet
found in the same Cluster.
The names are strings without whitespaces.
The values are lists of strings without whitespaces.

## Tags

### #facet_names

Present on all Gems, including the Aggregate 
Gem and Cluster Gems, the #facet_names tag
holds a list of all the facets used by that 
Gem.
