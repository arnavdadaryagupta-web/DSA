class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=len(t):
            return False
        unique_chars= set(s)
        for c in unique_chars:
            if s.count(c) != t.count(c):
                return False
        return True    

        