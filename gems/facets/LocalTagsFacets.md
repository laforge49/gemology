# LocalTagsFacets

The LocalTagsFacet and the #LocalTagIndexFacet together support
the use of locally scoped tags. The local tags of a gem are placed in
the LocalTagFacet held by each gem, while the #LocalTagIndexFacet
is held by a cluster and provides an index to all the gems in
that cluster.

The LocalTagsFacet is a dict whose keys are the Tag names and whose
values are lists of Tag values. (In a given gem, the same 
Tag can have more than one value.)

The #LocalTagIndexFacet is a 3-level tree of dicts and lists.
The first level is a dict whose keys are the Tag names, the values
being the dicts of the second level.
The keys of the second level are the Tag values, the values
being the lists of the third level.
The values held by the third level lists then are the gems
that have been tagged.
