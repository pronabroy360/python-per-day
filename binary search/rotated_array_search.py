def search(arr, n, k):
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2

        #if mid points to the target
        if mid == k:
            return mid
        
        #get the sorted half
        #if left is the sorted half
        if arr[low] <= arr[mid]:
            #if target is available
            if arr[low] <= k and k <= arr[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            if arr[mid] <= k and k<= arr[high]:
                low = mid +1
            else:
                high= mid-1
    return -1

if __name__ == "__main__":
    arr = [7,8,9,1,2,3,4,5]
    n = len(arr)
    k = 1
    ans = search(arr, n, k)
    print(ans)