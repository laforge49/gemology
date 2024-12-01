# Gems Facet

A GemsFacet holds a list of subordinate Gems.
A tree of Gems is formed from these subordinate Gems and the
Gems subordinate to them, recursively. The roots of these 
Gem trees are the Cluster Gems.

Cluster Gems (and the Aggregate Gem) 
are never held by a GemFacet.
And every non-Cluster Gem is a part of exactly one such 
Gem tree.
