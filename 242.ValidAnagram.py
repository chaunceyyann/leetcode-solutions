class Solution(object):
    def isAnagram(self, s, t):
        if len(s) == len(t) and len(s)!=0:
            alpha = [0] * 26
            beta = [0] * 26
            s=list(s)
            t=list(t)
            for i in range(len(s)):
                alpha[ord(s[i])-97]+=1
            for i in range(len(s)):
                beta[ord(t[i])-97]+=1
            if alpha == beta:
                return True
            else :
                return False
        elif len(s) == len(t) and len(s)==0:
            return True
        else :
            return False
