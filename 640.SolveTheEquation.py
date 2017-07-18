class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        def parser(part):
            coef,const = 0,0
            i,j = 0,0
            sign=1
            while i<len(part):
                if part[i]=='+':
                    sign=1
                elif part[i]=='-':
                    sign=-1
                elif part[i].isdigit():
                    j=i
                    while j<len(part) and part[j].isdigit():
                        j += 1
                    if j!=len(part):
                        if part[j]=='x':
                            coef+=int(part[i:j])*sign
                            i=j
                        else:
                            const+=int(part[i:j])*sign
                            i=j-1
                    else: 
                        const+=int(part[i:j])*sign
                        i=j-1
                else:
                    coef+=1*sign
                    
                i+=1
            return coef,const
        
        k1,b1 = parser(equation.split('=')[0])
        k2,b2 = parser(equation.split('=')[1])
        if b1==b2 or k1==k2:
            ans = "Infinite solutions"
            if b1!=b2:
                ans = "No solution"
            elif k1!=k2 :
                ans = "x=0"
        else :
            ans = "x=" + str((b2-b1)/(k1-k2))
                        
        return ans
