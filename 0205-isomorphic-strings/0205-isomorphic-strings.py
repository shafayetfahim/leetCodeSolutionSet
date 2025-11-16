from collections import Counter 
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s_t = {}
        map_t_s = {}

        for s_char, t_char in zip(s, t):
            if s_char in map_s_t and map_s_t[s_char] != t_char: return False
            if t_char in map_t_s and map_t_s[t_char] != s_char: return False
            map_s_t[s_char] = t_char
            map_t_s[t_char] = s_char
        return True
