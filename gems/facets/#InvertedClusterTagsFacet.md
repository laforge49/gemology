# #InvertedClusterTagsFacet

An #InvertedClusterTagsFacet indexes the tags in 
all the ClusterTagsFacets found
in that same Cluster Gem.
The #InvertedClusterTagsFacet holds a dict of the inverted Cluster tags, 
where the keys
of the dict are the tag names and the values are dicts whose keys are the
tag values. The values of these dicts are, in turn, lists of the gems
(references) which
hold the given Cluster tag name and value.

The #invertedClusterTagsFacet is generated when a PDML file is loaded.
This Facet can not be serialized as it would create circular references.
