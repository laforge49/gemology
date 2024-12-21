# Global Tags Facets

The GlobalTagsFacet and the #GlobalTagIndexFacet together support
the use of globally scoped tags. The global tags of a gem are
placed in
the GlobalTagFacet held by each gem, while the #GlobalTagIndexFacet
is held by the aggregate and provides an index to all gems.

The GlobalTagsFacet is a dict whose keys are the Tag names and whose
values are Tag values. (In a given gem, the same 
Tag can have only one value.)

The #GlobalTagIndexFacet is a 3-level tree of dicts and lists.
The first level is a dict whose keys are the Tag names, the values
being the dicts of the second level.
The keys of the second level are the Tag values, the values
being the lists of the third level.
The values held by the third level lists then are the gems
that have been tagged.

## Tag Names

### description

The value of this tag describes the gem which holds the tag.
