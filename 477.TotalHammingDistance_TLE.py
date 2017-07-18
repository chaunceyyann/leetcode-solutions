class Solution(object):
    
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def HammingDistance(a,b):
            return bin(a^b).count('1')
        s=0
        for i,x in enumerate(nums):
            for j in nums[i:]:
                s+=HammingDistance(x,j)
        return s
