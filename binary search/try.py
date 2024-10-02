class Solution:
    low = 0
    high = n-1
    def search(self, arr, n, k):
        

        while(low <= high):
            mid = (low+high)//2

            if mid == k:
                return True

            #lets find the sorted half
            if arr[low] <= arr[mid]:
                #find whether it is available
                if arr[low] <= k and k <= arr[mid]:
                    high = mid -1 
                else:
                    low = mid + 1
            else:
                if arr[mid] <= k and k <= arr[high]:
                    low = mid +1 
                else:
                    high = mid - 1
        return -1
if __name__ == "__main__":
    arr = [7, 8, 9, 1, 2, 3, 4, 5, 6]
    n = len(arr)
    k = 1
    obj = Solution()
    
    print(obj.search(arr,n,k))
    
