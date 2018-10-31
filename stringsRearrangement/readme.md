# Strings Rearrangement

## Problem

Given an array of equal-length strings, check if it is possible to rearrange the strings in such a way that after the rearrangement the strings at consecutive positions would differ by exactly one character.

## Examples

### Example 1

`stringsRearrangement(['cat','hat','try'])` will return False since there is no such reordering.

### Example 2

`stringsRearranement(['cat','mat','car','tar'])` will return True since `['tar','car','cat','mat']` is a valid rearrangement.

## Guaranteed Constraints

* Words will be lowercased and the same length.
* `2 ≤ len(inputArray) ≤ 10`
* `1 ≤ len(inputArray[i]) ≤ 15`


## Future Goals

Although the problem doesn't require it, it would be easy to return the maximal path in addition to the boolean -- and more helpful.

Note to self: Use an array `[boolean, maximal path]` where the maximal path is empty if boolean is `False`.
