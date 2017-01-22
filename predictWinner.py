<F11><F11>class Solution(object):
    def PredictTheWinner(self, nums):
        sum=[0,0]
        print "A",playerPick(nums,1,0,sum)
        sum=[0,0]
        print "A",playerPick(nums,1,-1,sum)

def playerPick(nums, player, pos, sum):
    print "*******"
    print nums
    print player,pos,sum
    if nums:
        if pos == 0:
            if player == 1:
                sum[0]+=nums[0]
                player=2
            else :
                sum[1]+=nums[0]
                player=1
            nums=nums[1:]
        if pos == -1:
            if player == 1:
                sum[0]+=nums[-1]
                player=2
            else :
                sum[1]+=nums[-1]
                player=1
            nums=nums[:-1]

        print "s1",sum
        print "st1",sum_t
        if playerPick(nums,player,0,sum):
            return True
        print "s2",sum
        print "st2",sum_t
        if playerPick(nums,player,-1,sum_t):
            return True
        print "false2"
        return False
    else :
        if sum[0]<sum[1]:
            print "false1"
            return False
        else:
            return True

