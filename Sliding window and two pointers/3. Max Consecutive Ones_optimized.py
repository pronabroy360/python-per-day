def flipZero(arr, k):
    count_of_zero = 0 
    max_len = 0
    r = 0
    l = 0
    
    for r in range(len(arr)):
        if arr[r] == 0:
            count_of_zero += 1 
        
        while count_of_zero > k:
            if arr[l] == 0:
               count_of_zero -= 1 
             
            l += 1                             # I once mistakenly put this l value within if loop. the answer comes fine as 1 less - result 8 coming as 7. you only move l forward when arr[l] == 0, which means if you encounter a 1 at l, the loop can get stuck.
                                               # For example, if arr[l] is 1, the code will never increase l in that loop, causing an infinite loop for certain inputs.
        
        max_len = max(max_len, r - l + 1)
    return max_len

if __name__ == "__main__":
    array = [1, 1, 1, 0, 0, 1, 1, 0]
    print(flipZero(array, 2))
