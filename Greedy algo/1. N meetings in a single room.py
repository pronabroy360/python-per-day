from typing import List

class Meeting:
    def __init__(self, start,end,pos):
        self.start = start
        self.end = end
        self.pos = pos

class Solution:
    def maxMeetings(self, s: List[int], e:List[int], n: int) -> None:
        meet = [Meeting(s[i], e[i], i+1) for i in range(n)]
        sorted(meet, key=lambda x: (x.end, x.pos))
        answer=[]
        limit = meet[0].end
        answer.append(meet[0].pos)
        for i in range(1,n):
            if meet[i].start > limit:
                
                answer.append(meet[i].pos)
                limit = meet[i].end
        print("The order in which the meetings will be performed is ")
        for i in answer:
            print(i, end=" ")

if __name__ == "__main__":
    obj = Solution()
    n=6
    start = [1,3,0,5,8,5]
    end = [2,4,5,7,9,9]
    obj.maxMeetings(start, end,n)