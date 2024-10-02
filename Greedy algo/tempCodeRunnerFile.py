from typing import List

def findContentChildren(greed, size):
    greed.sort()
    size.sort()
    n = len(greed)
    m = len(size)
    l=0
    r=0
    while l<len(size) and r < len(greed):
        if greed[r] <= size[l]:
            r+=1
        l+=1

    return r

if __name__ == "__main__":
    greed = [1,5,3,3,4]
    size = [4,2,1,2,1,3]
    ans = findContentChildren(greed, size)
    print(ans)