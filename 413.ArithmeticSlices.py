class Solution(object):
    def numberOfArithmeticSlices(self, A):
        if len(A)>2:
            cnt=2
            sum=0
            for i in range(len(A)):
                #print "i" ,i
                if i!=len(A)-2:
                    if A[i+2]-A[i+1] == A[i+1]-A[i]:
                        #print "cnt1",cnt
                        cnt+=1
                    else :
                        #print "cnt2",cnt
                        sum+=(cnt-2)*(cnt-1)/2
                        cnt=2
                else :
                    #print "cnt3",cnt
                    sum+=(cnt-2)*(cnt-1)/2
                    break
            return sum
        else :
            return 0