// https://leetcode.com/problems/longest-common-prefix

from collections import Counter

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        if not strs:
            return common_prefix
        is_common = True
        i = 0
        min_len = min(map(len, strs))
        while is_common and i < min_len:
            is_common = len(set([s[i] for s in strs])) == 1
            if is_common:
                common_prefix += strs[0][i]
            i+=1
        return common_prefix

        