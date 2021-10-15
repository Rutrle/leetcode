class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_map = {}
        for i in range(len(s)):
            if s[i] not in char_map and t[i] in char_map.values():
                return False
            if s[i] not in char_map:
                char_map[s[i]] = t[i]

            elif char_map[s[i]] != t[i]:
                return False
        return True
