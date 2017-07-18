class Solution(object):
    def hammingDistance(self, x, y):
        cnt = 0
        n=x^y
        while n>0:
            cnt += 1
            n = n&(n-1)
            
        return cnt

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')
