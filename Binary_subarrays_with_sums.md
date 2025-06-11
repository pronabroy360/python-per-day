
---

# 📘 Guidebook: Binary Subarrays With Sum (Goal)

---

## 📌 Problem Statement

You are given a **binary array** (`nums[]`) and an **integer goal**. Your task is to **count the number of subarrays** such that the **sum of elements** in each subarray is **exactly equal** to the `goal`.

### 🧾 Definitions

* **Binary array** = contains only 0s and 1s.
* **Subarray** = a contiguous portion of an array.
* **Sum** = sum of elements within the subarray.

---

## 🎯 Example

```plaintext
nums = [1, 0, 1, 1, 0], goal = 2

Valid subarrays with sum = 2:
[1, 0, 1], [0, 1, 1], [1, 1], [1, 1, 0]

=> Output = 4
```

---

## 🧠 Intuition

The classic solution for counting subarrays with sum = K involves a **prefix sum + hashmap**, which works even for negative numbers.

But since this array only contains **0s and 1s**, we can **optimize** the space using a **two-pointer or sliding window** technique.

---

## ⚙️ Step-by-Step Strategy

### ✅ Step 1: Understand That “Equal to K” is Tricky

Tracking exact `sum == goal` is hard with a sliding window, especially with 0s in the array (which don’t change the sum when shrinking the window).

### ✅ Step 2: Relax the Problem

Instead of directly counting subarrays with `sum == goal`, count:

```
count_subarrays(sum <= goal) - count_subarrays(sum <= goal - 1)
```

This works because:

* `count_subarrays(sum <= goal)` includes all sums up to `goal`
* `count_subarrays(sum <= goal - 1)` includes all sums less than `goal`

So the **difference** gives you **exactly sum == goal**.

---

## 🔍 Subproblem: Count Subarrays With Sum ≤ Goal

We’ll define a function `atMost(goal)` which counts subarrays with sum **≤ goal**.

### 🎯 Logic:

* Use two pointers: `left`, `right`
* Expand `right` and add to sum
* If `sum > goal`, shrink window from the `left` until `sum ≤ goal`
* Each valid window \[left, right] adds `(right - left + 1)` subarrays

### ⛔ Edge Case:

If `goal < 0`, return 0 (invalid for binary arrays with only 0s and 1s)

---

## 💻 Final Algorithm

### 🔧 Python Code

```python
def numSubarraysWithSum(nums, goal):
    def atMost(S):
        if S < 0:
            return 0
        left = 0
        total = 0
        res = 0
        for right in range(len(nums)):
            total += nums[right]
            while total > S:
                total -= nums[left]
                left += 1
            res += (right - left + 1)
        return res

    return atMost(goal) - atMost(goal - 1)
```

---

## 🧮 Time and Space Complexity

| Operation | Complexity                               |
| --------- | ---------------------------------------- |
| Time      | **O(N)** (2 passes of the array)         |
| Space     | **O(1)** (no extra data structures used) |

> `N` = length of the array

---

## 📊 Comparison With Other Approaches

| Approach              | Time  | Space | Notes                         |
| --------------------- | ----- | ----- | ----------------------------- |
| Brute Force           | O(N²) | O(1)  | Generates all subarrays       |
| Prefix Sum + HashMap  | O(N)  | O(N)  | Optimal for +ve/-ve integers  |
| Sliding Window (this) | O(N)  | O(1)  | Works because input is binary |

---

## ✅ Test Cases

### 🔸 Basic

```python
nums = [1,0,1,1,0]; goal = 2
# Output: 4
```

### 🔸 Edge Case: All Zeros

```python
nums = [0,0,0,0]; goal = 0
# Output: 10 (n*(n+1)/2 subarrays)
```

### 🔸 Edge Case: No valid subarrays

```python
nums = [1,1,1,1]; goal = 0
# Output: 0
```

---

## 🧠 Insights

* This approach works **only** for non-negative integers.
* We optimize **space** by **removing the map** from the hashmap solution.
* The key idea is **reducing an exact condition** (`sum == goal`) into two **at most** conditions (`sum ≤ goal` and `sum ≤ goal-1`).

---

## 📌 Summary

* Problem = Count subarrays with **sum = goal** in a **binary array**
* Convert to `count(sum ≤ goal) - count(sum ≤ goal - 1)`
* Use **sliding window** to compute `count(sum ≤ X)`
* Achieve **O(N) time** and **O(1) space**

---
