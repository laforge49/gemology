# #InvertedAggregateIdsFacet

An #InvertedAggregateIdsFacet indexes the Ids
in all the AggregateTagsFacets found
in all the Cluster Gems.
The #InvertedAggregateIdsFacet holds a dict
of the inverted Aggregate ids, 
where the keys
of the dict are the Id types and the values 
are dicts whose keys are the
Ids. The values of these dicts are, 
in turn, the gems
(references) which
hold the given Aggregate Id.

The #invertedAggregateIdsFacet is updated 
when a PDML file is loaded.
This Facet can not be serialized as it would 
create circular references.
