class Solution(object):
    def judgeCircle(self, moves):
        v,h=0,0
        for c in moves:
            if c == "U": v+=1
            if c == "D": v-=1
            if c == "R": h+=1
            if c == "L": h-=1
        return True if v == 0 and h ==0 else False
