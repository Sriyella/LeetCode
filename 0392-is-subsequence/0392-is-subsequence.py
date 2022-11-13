class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        b = 0
        if len(s) == 0:
            return True
        for i, a in enumerate(t):
            if a == s[b]:
                if b == len(s) - 1:
                    return True
                else:
                    b += 1
            else:
                continue
        return False