# from typing import List

# class Solution:
#     def subsetSums(self, arr: List[int], n:int) -> List[int]:
#         ans=[]
#         def substetSumsHelper(ind: int, sum:int):
#             if ind == n:
#                 ans.append(sum)
#                 return 
#             #element is picked
#             substetSumsHelper(ind+1, sum + arr[ind])

#             #element is not picked
#             substetSumsHelper(ind+1, sum)
#         substetSumsHelper(0,0)
#         ans.sort()
#         return ans
    
# if __name__=="__main__" :
#     arr=[3,1,2]
#     ans= Solution().subsetSums(arr,len(arr))
#     print("The sum of each subset is")
#     for sum in ans:
#         print(sum, end=" ")
#     print()

##################################################2nd attempt

# from typing import List

# class Solution():
#     def subsetSum(self, arr, N): # I got an error here; I had to add self as non-static methods usually takes self as first argument and i were giving arr, N only 2 arguments.
#         ans = []
#         def subsetSumsHelper(ind, sum):
#             if ind == N:
#                 ans.append(sum)
#                 return
            
#             #pick it
#             subsetSumsHelper(ind+1, sum+ arr[ind])

#             #not pick it
#             subsetSumsHelper(ind+1, sum)
        
#         subsetSumsHelper(0,0)
#         ans.sort()
#         return ans

# if __name__ == "__main__":
#     arr=[3,1,2]
#     N=3
#     ans = Solution().subsetSum(arr, N)
#     print(ans, end=" ")


from typing import List

class Solution:
    def subsetSum(self, arr, N):
        ans=[]
        def subsetSumHelper(ind,sum):
            if ind == N:
                ans.append(sum)
                return
            
            #pick
            subsetSumHelper(ind+1, sum + arr[ind])

            #not pick
            subsetSumHelper(ind+1, sum)
        subsetSumHelper(0,0)
        ans.sort()
        return ans
if __name__ == "__main__":
    arr=[2,4,1,5]
    N=len(arr)
    print(Solution().subsetSum(arr,N))