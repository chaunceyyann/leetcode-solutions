class Solution(object):
    def totalHammingDistance(self, nums):
        bits = [ [0,0] for _ in xrange(32) ]
        #bits = [ [0,0] ] * 32   ??????? why not work ???????
        for x in nums:
            for i in xrange(32):
                bits[i][x%2] += 1
                x /= 2
        return sum( x*y for x,y in bits )
