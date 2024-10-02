# from typing import List

# class Solution:
#     def Solver(self, s):
#         ans = []
#         init = []

#         def helperFunc(ind):
#             if ind == len(s):
#                 ans.append(init[:])
#                 return
            
#             for i in range(ind, len(s)):
#                 if isPalindrome(s, ind, i):
#                     init.append(s[ind:i+1]) #as the slicing in python is inclusive
#                     helperFunc(i+1)
#                     init.pop()
        
#         def isPalindrome(string, start, end):
#             while start <= end:
#                 if string[start] != string[end]:
#                     return False
#                 start += 1
#                 end -= 1
            
#             return True
        
#         helperFunc(0)
#         return ans
    
# if __name__ == "__main__":
#     s = "aabb"
#     obj = Solution()
#     ans = obj.Solver(s)
#     print(ans)


from typing import List

class Solution:
    def solver(self, s):
        ans = []
        path = []
        def helperFunc(ind):
            #base condition
            if ind == len(s):
                ans.append(path[:])
                return
            for i in range(ind, len(s)):
                if isPalindrome(s, ind, i):
                    path.append(s[ind:i+1])
                    helperFunc(i+1)
                    path.pop()
    
        def isPalindrome(s, start, end):
            while start <= end:
                if s[start] !=  s[end]:
                    return False
                start += 1
                end -= 1

            return True
        
        helperFunc(0)
        return ans

if __name__ == "__main__":
    s = "aabb"
    obj = Solution()
    ans = obj.solver(s)
    print(ans)