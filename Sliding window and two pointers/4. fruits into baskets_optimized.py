## fruit into baskets 
## arr = [2 , 2, 3, 2, 2, 4, 4, 4, 4]
## k = 2

from collections import defaultdict

def fruit_into_baskets(arr, k):
    l = 0 
    r = 0 
    max_len = 0
    
    counter = defaultdict(int)
    
    for r in range(len(arr)):
        
        counter[arr[r]] += 1
        
        while len(counter) > k:
            counter[arr[l]] -= 1 
            if counter[arr[l]] == 0:
                del counter[arr[l]]
            l += 1 
        max_len = max(max_len, r - l + 1)
    return max_len

arr = [2, 2, 3, 2, 2, 4, 4, 4, 4]
k = 2
ans = fruit_into_baskets (arr, k)
print(ans)
