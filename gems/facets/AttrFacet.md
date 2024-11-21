# AttrFacet

An AttrFacet holds a dict of attribute name/value pairs.
The names are strings without whitespace. The values are
python scalars (including multi-line strings), lists and
dicts, recursively.

## Attributes

### #cluster

Present on neither the Aggregate Gem nor on
any Cluster Gems, the #cluster attribute 
holds a reference to the Cluster which this
Gem is a part.

### #cluster_path

Present only on Cluster Gems, the 
#cluster_path attribute holds the pathname 
of the file from which the Cluster Gem was
loaded.

### #gem_parent

Present on neither the Aggregate Gem nor on
any Cluster Gems, the #gem_parent
attribute holds a reference to the Gem or
Cluster Gem that the Gem is subordinate to.