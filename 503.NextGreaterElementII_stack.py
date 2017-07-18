class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        stack=[]
        res=[0]*n
        for i in range(2*n-1,-1,-1):          
            res[i%n]=-1
            while len(stack):
                top=stack[-1]
                if nums[top]>nums[i%n]:
                    res[i%n]=nums[top]
                    break
                else:
                    stack=stack[:-1]#pop
                    res[i%n]=-1
            stack.append(i%n)    
            #print "stack",stack
            #print "res",res
        return res
