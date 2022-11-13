class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sc = dict()
        tc = dict()
        flag = 0
        for i, l in enumerate(s):
            if l not in sc and t[i] not in tc:
                sc[l] = t[i]
                tc[t[i]] = l
            elif (l in sc) ^ (t[i] in tc):
                return False
            #print(i, sc[l], tc[t[i]])
            if sc[l] == t[i] and tc[t[i]] == l:
                continue
            else:
                return False
        return True
        