class Solution(object):
    def countSubstrings(self, s):
        n=len(s)
        c=n
        for i in range(n):
            if i<(n//2) :
                r=i
            else:
                r=n-i-1 

            for j in range(1,r+1):
                #print "j", j
                if s[i+j]==s[i-j]:
                    c+=1
                else:
                    break
                    
        for i in range(n-1):
            if s[i]==s[i+1]:
                c+=1
                if i<(n//2):
                    r=i
                else:
                    r=n-i-2
                for j in range(1,r+1):
                    if s[i+1+j]==s[i-j]:
                        c+=1
                    else:
                        break    
        return c
