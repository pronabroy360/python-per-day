from typing import List

class Solution:
    def CombinationSum(self, arr, target):
        ans = []
        ds = []

        def helperFunction(ind, target):
            if ind == len(arr):
                if target == 0:
                    ans.append(ds[:])
                return

            if arr[ind] <= target:
                ds.append(arr[ind])
                helperFunction(ind, target-arr[ind])
                ds.pop()
            helperFunction(ind+1,target)
        arr.sort()
        helperFunction(0, target)
        return ans

if __name__ == "__main__":
    arr = [2,2,3,7]
    target = 7
    obj = Solution()
    print(obj.CombinationSum(arr, target))