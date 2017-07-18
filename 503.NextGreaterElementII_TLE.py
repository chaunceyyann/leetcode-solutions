class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        rtn=[]
        for i in range(n):
            rtn.append(-1)
            for j in range(i,n+i):
                if nums[i]<nums[j%n]:
                    rtn[i]=nums[j%n]
                    break
        return rtn
