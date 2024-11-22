# ClusterIdFacet

A ClusterTagsFacet holds a dict of Id name/value pairs.
These are indexed in the #InvertedClusterTagsFacet
found in the same Cluster.
The names are strings without whitespaces.
The values are strings without whitespaces.

## Ids

### gem_base_name

Present on neither the Aggregate Gem nor on
any Cluster Gem, but present on all other 
Gems, the gem_base_name Id holds the local
name of a Gem.

Local Gem names are unique within the scope
of a Cluster. Full Gem names are constructed
from a Cluster Gem name, "." and the local
Gem name.
