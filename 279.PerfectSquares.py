class Solution(object):
    def numSquares(self, n):
        if n>0:
            m=int(math.sqrt(n))
            #print m
            s=[]
            s.append(n)
            cnt=0
            num=n
            #print s
            for i in range(2,m+1):
                print "i",i
                for j in range(i,1,-1):
                    cnt+=num/pow(j,2)
                    diff=num%pow(j,2)
                    print "cnt",cnt
                    print "diff",diff
                    if diff>3:
                        num=diff
                    else :
                        s.append(cnt+diff) 
                        break
                    if diff<4 and diff>0:
                        s.append(cnt+diff) 
                        break
                
                cnt=0
                num=n
                    
            print s
            print 
            return min(s)
        else :
            return 0

        
