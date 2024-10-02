from typing import List

class Solution:
    def recurPermute(self, nums):
        ans = []
        def helperFunction(ind, nums):
            if ind == len(nums):
                ans.append(nums[:])
                return
            
            for i in range(ind, len(nums)):
                nums[ind], nums[i] = nums[i], nums[ind]
                helperFunction(ind+1, nums)
                nums[ind], nums[i] = nums[i], nums[ind]
        helperFunction(0, nums)
        return ans

if __name__ == "__main__":
    obj = Solution()
    v=[1,2,3]
    ans = obj.recurPermute(v)
    print(ans)