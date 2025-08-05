def print_consecutive_ones(arr, k):
    r =  0
    l = 0
    maxLen = 0 
    
    for r in range(len(arr)):
        zeros = 0
        if arr[r] == 0:
            zeros += 1
        
        if zeros > k:
            if arr[l] == 0:
                zeros -= 1 
            
            l += 1  
        maxLen = max(maxLen, r - l + 1)
    return maxLen


if __name__ == "__main__":
    arr = [1, 1, 1, 0, 0, 1, 1, 0]
    print(print_consecutive_ones(arr, 2))
