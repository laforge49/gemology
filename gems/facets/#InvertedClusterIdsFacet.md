# #InvertedClusterIdsFacet

An #InvertedClusterIdEntriesFacet indexes the Ids in 
all the ClusterIdsFacets found
in that same Cluster Gem.
The #InvertedClusterIdEntriesFacet holds a type dict 
where the keys of the type dict are the Id types.
The values held by the type dict are Id dicts
where the keys of the Id dicts are Id names.
and the values are dicts whose keys 
are the
Id values. The values of these dicts are, in turn, the gems
(references) which
hold the given Cluster Id.

The #invertedClusterIdsFacet is generated when a PDML file is loaded.
This Facet can not be serialized as it includes circular 
references.
