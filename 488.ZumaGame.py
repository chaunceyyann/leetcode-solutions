class Solution(object):
    def findMinStep(self, board, hand):
        wn,rn,bn,yn,gn = 0,0,0,0,0
        b=list(board)
        h=list(hand)
        wn=b.count("W")
        rn=b.count("R")
        bn=b.count("B")
        yn=b.count("Y")
        gn=b.count("G")
        print wn,rn,bn,yn,gn
        for i in range(len(b)):
            if b[i]==b[i+1]:
                try:
                    hloc=h.index(b[i])
                except:
                    return -1
                del b[i]
                del b[i]
                del h[hloc]
                i-=1
            else :
                if h.count(b[i])>1:
                    h.remove(b[i])
                    h.remove(b[i])
                    del b[i]
                elif h.count(b[i])==1
                    if b.count(b[i])>1
                else:
                    return -1
                    
                    
