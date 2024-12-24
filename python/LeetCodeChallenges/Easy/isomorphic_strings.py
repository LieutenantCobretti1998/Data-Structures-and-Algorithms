# Todo Given two strings s and t, determine if they are isomorphic
#  Two strings s and t are isomorphic if the characters in s can be replaced to get t.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        "egg add"
        s_to_t = {}
        t_to_s = {}

        for c1, c2 in zip(s, t):
            if c1 in s_to_t:
                if s_to_t[c1] != c2:
                    return False
            else:
                s_to_t[c1] = c2

            if c2 in t_to_s:
                if t_to_s[c2] != c1:
                    return False
            else:
                t_to_s[c2] = c1

        return True

# Time and Space complexity is O(n)