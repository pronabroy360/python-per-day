from typing import List

class Solution:
    def subsetSumBrut(self, nums):
        ans = []
        res = set()

        def subsetHelper(ind:int, ds:List[int]):
            if ind == len(nums): #If the ind (current index) is equal to the length of nums, this means we've reached the end of the list and generated a subset.
                ds.sort() # ensures that any duplicate subsets (in terms of elements) are added to res in the same order, preventing duplicates.
                res.add(tuple(ds)) #The current subset (ds) is converted into a tuple (tuple(ds)) before adding it to the set res, since sets can only store hashable objects like tuples.
                return
            ds.append(nums[ind]) #(Include nums[ind] in subset):First, nums[ind] is added to ds (i.e., the current subset), and the recursive function is called with ind + 1, moving to the next index.
            subsetHelper(ind+1, ds) # (Backtrack):After the recursive call, the last element added to ds is removed using ds.pop(), so we can explore the subsets that do not include nums[ind].
            ds.pop() #(Exclude nums[ind]):After backtracking, we make another recursive call without including nums[ind] to generate the subsets that exclude this element.
            subsetHelper(ind+1, ds)
        subsetHelper(0, [])
        for it in res:
            ans.append(list(it)) #Each tuple in res is converted back into a list and added to ans, since the final result needs to be in list format.
        return ans

if __name__ == "__main__":
    nums=[1,2,2]
    obj = Solution()
    ans = obj.subsetSumBrut(nums)
    print(ans)

