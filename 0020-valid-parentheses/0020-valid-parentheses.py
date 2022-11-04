class Solution:
    def isValid(self, s: str) -> bool:
        b = {'(':')', '[':']', '{':'}'}
        o = list()
        for i in s:
            if i==0:
                if i in b:
                    o.append(i)
                else:
                    return False
            else:
                if i in b:
                    o.append(i)
                else:
                    if len(o)>0:
                        if i==b[o[-1]]:
                            o = o[:-1]
                        else:
                            return False
                    else:
                        return False
        if len(o)==0:
            return True
        else:
            return False