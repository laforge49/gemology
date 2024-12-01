# Global Ids Facets

The GlobalIdsFacet and the #GlobalIdIndexFacet together support
the use of globally scoped identifiers with gems. The ids of a 
gem are placed in
the GlobalIdFacet held by each gem, while the 
#GlobalIdIndexFacet
is held by the aggregate and provides an index to all gems.

The GlobalIdsFacet is a dict whose keys are the Id types and whose
values are the Id names. 
The #GlobalIdIndexFacet is a 2-level tree of dicts. The keys of the
first level are the Id types, the keys of the second level are the
Id names, and the values of the second level are the gems for the
given Id type and name.

## Id types

### #cluster_name

Present only on Cluster Gems, the 
#cluster_name holds the name of that 
Cluster Gem.
