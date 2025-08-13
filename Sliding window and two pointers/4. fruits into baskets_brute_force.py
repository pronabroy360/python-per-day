###fruit into baskets
### [1, 1, 2, 2, 2, 3, 4, 4, 4]
### k = 2 


from collections import defaultdict

def fruit_into_baskets (arr, k):
    max_len = 0
    
    for i in range(len(arr)):
        
        counter = defaultdict(int)
        for j in range(i, len(arr)):
            counter[arr[j]] += 1
            if len(counter) > k:
                break 
            max_len = max(max_len, j - i + 1)
    return max_len

arr = [1, 1, 2, 2, 2, 3, 4, 4, 4]
k = 2
ans = fruit_into_baskets (arr, k)
print(ans)
