class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return [] 
        else :
            rtn=[matrix[0][0]]
            m=len(matrix)
            n=len(matrix[0])
            i,j=0,0 # m,i -> rows . n,j -> colums
            di=0    # 0 -> up, 1 -> down 
            while len(rtn)<m*n:
                if not di:
                    di=1
                    if i-1<0 and j+1<n:     #case1
                        j+=1
                    elif j+1>=n:            #case2
                        i+=1
                    else :                  #normal
                        i-=1
                        j+=1
                        di=0
                else:
                    di=0
                    if j-1<0 and i+1<m:     #case3
                        i+=1
                    elif i+1>=m:            #case 4
                        j+=1
                    else :                  #normal
                        i+=1
                        j-=1
                        di=1
                rtn.append(matrix[i][j])
            return rtn
