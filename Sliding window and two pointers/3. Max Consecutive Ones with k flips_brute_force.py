def flipZero(arr, k):
    maxlen = 0
    for i in range(len(arr)):
        zeros = 0
        for j in range(i, len(arr)):
            if arr[j] == 0:
                zeros += 1
            
            if zeros > k:
                break 
            
            maxlen = max(maxlen, j - i + 1)
    return maxlen

if __name__ == "__main__":
    array = [1, 1, 1, 0, 0, 1, 1, 0]
    print(flipZero(array, 2))
