class Solution(object):
    def threeSumClosest(self, nums, target):
        dic={}
        if len(nums)>2:
            for i in range(len(nums)-2):
                for j in range(i+1,len(nums)-1):
                    for k in range(j+1,len(nums)):
                        s=nums[i]+nums[j]+nums[k]
                        if dic.has_key(s):
                            break
                        else:
                            dic[s]=[abs(s-target)]
            
            ls=sorted(dic.items(), key=lambda x: x[1])
            
            return ls[0][0]
                        
        
