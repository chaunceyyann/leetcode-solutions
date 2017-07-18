class Solution(object):
    def findDiagonalOrder(self, matrix):
        direction="u"
        i,j=0,0
        if matrix:
            rtn=[matrix[i][j]]
            M=len(matrix)
            N=len(matrix[0])
            while len(rtn)<=M*N:

                if i==M-1 and j==N-1:
                    break
                if direction=="u":
                    if i-1<0 and j+1<N:
                        direction="d"
                        j=j+1
                    elif j+1>=N:
                        i=i+1
                        direction="d"
                    else :
                        i=i-1
                        j=j+1
                
                        
                elif direction=="d":
                    if j-1<0 and i+1<M:
                        direction="u"
                        i=i+1
                    elif i+1>=M:
                        j=j+1
                        direction="u"
                    else :
                        i=i+1
                        j=j-1
                #print "ij",i,j
                #print "d",direction
                #print matrix[i][j]
                rtn.append(matrix[i][j])
                
                
            return rtn
        else:
            return []
