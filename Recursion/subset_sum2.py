from typing import List

class Solution:
    def subsetWithDup(self, nums):
        ans = []
        ds = []

        def findSubsets(ind):
            ans.append(ds[:]) #The current subset (ds[:]) is added to ans. Here ds[:] creates a shallow copy of the current subset to avoid mutation during recursion.
            for i in range(ind, len(nums)):
                # This condition ensures that duplicates are skipped. If the current number is the same as the previous one (nums[i] == nums[i-1]) and it's not the first iteration in the current recursion (i.e., i != ind), the loop continues without including the duplicate element.
                if i!= ind and nums[i] == nums[i-1]:
                    continue
                
                ds.append(nums[i])
                findSubsets(i+1)
                ds.pop()
        nums.sort()
        findSubsets(0)
        return ans

if __name__ == "__main__":
    nums = [1,2,2]
    obj = Solution()
    ans = obj.subsetWithDup(nums)
    print(*ans)