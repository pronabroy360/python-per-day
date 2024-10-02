def countPlatforms(arr,dep,n):
    arr.sort()
    dep.sort()

    ans = 1
    count=1
    i=1
    j=0

    while i< n and j <n:
        if arr[i] <= dep[j]:
            count += 1
            i+=1
        else:
            count -= 1
            j+=1
        ans = max(count,ans)
    return ans

if __name__ == "__main__":
    arr = [900,945,955,1100,1500,1800]
    dep = [920,1200 , 1130, 1150, 1900, 2000]
    print(countPlatforms(arr,dep,6))