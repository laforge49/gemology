# AggregateTagsFacet

A AggregateTagsFacet holds a dict of Tag name/value pairs.
These are indexed in the #InvertedAggregateTagsFacet
found in the Aggregate Gem.
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

### #ClusterName

Present only on Cluster Gems, the 
#ClusterName tag holds the name of that 
Cluster Gem.
