# #InvertedAggregateTagsFacet

An #InvertedAggregateTagsFacet indexes the tags
in all the AggregateTagsFacets found
in all the Cluster Gems.
The #InvertedAggregateTagsFacet holds a dict
of the inverted Aggregate tags, 
where the keys
of the dict are the tag names and the values 
are dicts whose keys are the
tag values. The values of these dicts are, 
in turn, lists of the gems
(references) which
hold the given Aggregate tag name and value.

The #invertedAggregateTagsFacet is updated 
when a PDML file is loaded.
This Facet can not be serialized as it would 
create circular references.
