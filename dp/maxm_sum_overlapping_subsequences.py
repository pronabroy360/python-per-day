# #rule 1: in terms of index:
# #f(ind)
# def solve(ind, arr, dp):
# #rule 2: do all possible stuffs on that idx:
# # base condn
# # if ind == 0: return arr[0]
#     if ind==0: return arr[ind]
#     if ind<0: return 0
#     if dp[ind]!= -1:
#         return dp[ind]
#     #pick
#     pick = arr[ind] + solve(ind-2, arr,dp) 
#     #nonPick
#     Nonpick = 0+solve(ind-1, arr, dp)
#     dp[ind] = max(pick, Nonpick)
#     return dp[ind]

# if __name__ == "__main__":
#     arr = [2,1,4,9]
#     n = len(arr)
#     dp = [-1]* (n+1)
#     ans= solve(n-1, arr, dp)
#     print(ans)


## using dp
# #rule 1: in terms of index:
# #f(ind)
def solve(ind, arr, dp):
#rule 2: do all possible stuffs on that idx:
# base condn
# if ind == 0: return arr[0]
    if ind==0: dp[0] = arr[0]
    if ind<0: return 0
    if dp[ind]!= -1:
        return dp[ind]
    for i in range(1, n):
        #pick
        pick = arr[i] + solve(i-2, arr,dp) 
        #nonPick
        Nonpick = 0+solve(i-1, arr, dp)
        dp[i] = max(pick, Nonpick)
    return dp[n-1]

if __name__ == "__main__":
    arr = [5,3,4,1]
    n = len(arr)
    dp = [-1]* (n+1)
    ans= solve(n-1, arr, dp)
    print(ans)
