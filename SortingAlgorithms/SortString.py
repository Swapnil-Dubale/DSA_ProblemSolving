'''nput: s = "edcab"
Output: "abcde"
Explanation: characters are in ascending order in "abcde".

Input: s = "xzy"
Output: "xyz"
Explanation: characters are in ascending order in "xyz".'''

## Builtin Sort - O(n log n) Time O(1) Space
str = "acbdc"
print(''.join(sorted(str)))
