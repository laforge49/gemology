# #InvertedClusterIdsFacet

An #InvertedClusterIdsFacet indexes the Ids in 
all the ClusterIdsFacets found
in that same Cluster Gem.
The #InvertedClusterIdsFacet holds a dict of the inverted Cluster Ids, 
where the keys
of the dict are the Id types and the values are dicts whose keys are the
Id values. The values of these dicts are, in turn, the gems
(references) which
hold the given Cluster Id.

The #invertedClusterIdsFacet is generated when a PDML file is loaded.
This Facet can not be serialized as it would create circular references.
