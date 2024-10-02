# from typing import List

# class Solution:
#     def CombinationSum(self, arr, target):
#         ans = []
#         ds = []
#         def helperFunc(ind, target):
#             if target == 0:
#                 ans.append(ds[:])
#                 return
#             for i in range(ind, len(arr)):
#                 if arr[i] == arr[i-1] and i > ind:
#                     continue
#                 if arr[i] > target:
#                     break
#                 ds.append(arr[i])
#                 helperFunc(i+1, target - arr[i])
#                 ds.pop()
#         arr.sort()
#         helperFunc(0, target)
#         return ans

# if __name__ == "__main__":
#     arr = [1,1,1,2,2]
#     target = 4
#     obj = Solution()
#     print(obj.CombinationSum(arr, target))

from typing import List

class Solution:
    def combinationSum(self, arr, target):
        ans = []
        ds = []
        def helperFunc(ind,target):
            if target == 0:
                ans.append(ds[:])
                return
            for i in range(ind):
                if i>ind and arr[i]==arr[i-1]:
                    continue
                if arr[i] > target:
                    break
                ds.append(arr[i])
                helperFunc(i+1, target- arr[i])
                ds.pop()
            arr.sort()
            helperFunc(0, target)
            return ans

if __name__ == "__main__":
    arr = [1,1,1,2,2]
    target = 4
    obj = Solution()
    print(obj.CombinationSum(arr, target))