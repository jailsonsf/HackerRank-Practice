# Sets

## Operators

| Operation | Equivalent | Result |
| ----------|:-----------|:-------|
| `len(s)` | | number of elements in set s |
| `x in s` | | test x for membership in s |
|`x not in s`| | test x for non-membership in s |
| `s.issubset(t)` | `s <= t` | test whether every element in s is in t |
| `s.issuperset(t)`| `s >= t` | test whether every element in t is in s |
| `s.union(t)` | `s | t` | new set with elements from both s and t |
| `s.intersection(t) `| `s & t` | new set with elements common to s and t |
