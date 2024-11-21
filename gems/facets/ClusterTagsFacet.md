# ClusterTagsFacet

A ClusterTagsFacet holds a dict of Tag name/value pairs.
These are indexed in the #InvertedClusterTagsFacet
found in the same Cluster.
The names are strings without whitespace.
The names are strings without whitespace.
The values are python scalars. The values may include neither
lists nor dicts.

## Tags

### gem_base_name

Present on neither the Aggregate Gem nor on
any Cluster Gem, but present on all other 
Gems, the gem_base_name tag holds the local
name of a Gem.

Local Gem names are unique within the scope
of a Cluster. Full Gem names are constructed
from a Cluster Gem name, "." and the local
Gem name.

### #facet_names

Present on all Gems, including the Aggregate 
Gem and Cluster Gems, the #facet_names tag
holds a list of all the facets held by that 
Gem.
