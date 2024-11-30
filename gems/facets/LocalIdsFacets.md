# Local Ids Facets

The LocalIdsFacet and the #LocalIdIndexFacet together support
the use of identifiers with gems. The ids of a gem are placed in
the LocalIdFacet held by each gem, while the #LocalIdIndexFacet
is held by a cluster and provides an index to all the gems in
that cluster.

The LocalIdsFacet is a dict whose keys are the Id types and whose
values are the Id names. 
The #LocalIdIndexFacet is a 2-level tree of dicts. The keys of the
first level are the Id types, the keys of the second level are the
Id names, and the values of the second level are the gems for the
given Id type and name.

## Id types

### gem_base_name

Present on neither the Aggregate Gem nor on
any Cluster Gem but present on all other 
Gems, the gem_base_name holds the base
name of a Gem.

Base Gem names are unique within the scope
of a Cluster. Full Gem names are constructed
from a Cluster name, "." and the base
Gem name.
