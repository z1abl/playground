# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.

from typing import List

class Solution:
    def longestCommonPrefixOne(self, strs: List[str]) -> str:
        first_word = strs[0]
        edge = len(first_word)
        i = edge
        while i > 0:
            prefix = first_word[:i]
            count = sum(map(lambda x: x.startswith(prefix), strs[1:]))
            if count == len(strs[1:]):
                return prefix
            i-=1
        return ""

    def longestCommonPrefixTwo(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        common_prefix = ''
        first_word = strs[0]
        i=1
        while i<=len(first_word):
            prefix = first_word[:i]
            edge = len(strs)-1
            for word in strs[1:]:
                if word.startswith(prefix):
                    edge-=1
                    if edge == 0:
                        common_prefix = prefix
                else:
                    if common_prefix:
                        return common_prefix
            i+=1
        return common_prefix

    def longestCommonPrefixThree(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        first_word = strs[0]
        i = 0
        while i < len(first_word):
            char = first_word[i]
            index = 0
            for word in strs[1:]:
                if i<len(word) and word[i] == char:
                    index+=1
            if index < len(strs[1:]):
                return first_word[:i]
            i+=1
        return first_word[:i] if first_word[:i] else ''

