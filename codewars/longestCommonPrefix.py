'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.

class Solution:
    def longestCommonPrefix(strs):
        pass
'''

class Solution:
    def longestCommonPrefix(strs):
        maximum = len(min(strs, key=len))
        t = set([i[:maximum] for i in strs])
        if len(t) == 1 or len(strs) == 1:
            return next(iter(t))
        else:
            while True:
                if len(t) == 1:
                    return next(iter(t))
                else:
                    t = set([i[:maximum] for i in t])
                    maximum -= 1


assert Solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
assert Solution.longestCommonPrefix(["dog", "racecar", "car"]) == ""
assert Solution.longestCommonPrefix([""]) == ""
assert Solution.longestCommonPrefix(["", ""]) == ""
assert Solution.longestCommonPrefix(["ab", "a"]) == "a"
assert Solution.longestCommonPrefix(["flower", "flower", "flower", "flower"]) == "flower"
assert Solution.longestCommonPrefix(["abab", "aba", ""]) == ""
