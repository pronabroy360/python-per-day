# **Two-Pointer & Sliding Window Techniques**  
### *A Comprehensive Guide for Problem Solving*

---

## **1. Introduction**
The **two-pointer** and **sliding window** techniques are powerful problem-solving strategies in programming and algorithmic interviews. They allow efficient traversal and manipulation of arrays, strings, and other sequences. Unlike memorizing specific algorithms, these methods require understanding **how to dynamically adjust pointers/windows** based on conditions.

### **Key Takeaways**
✔ **Not memorization-based**—depends on pattern recognition & adaptability.  
✔ Enhances **time complexity** from brute-force (O(n²)) to optimized (O(n)).  
✔ Used in **arrays**, **strings**, **linked lists**, and **subarray/substring problems**.  

---

## **2. Four Problem Patterns**
Four common patterns where these techniques are applied:

### **Pattern 1: Constant-Size Window (Fixed-Length Subarrays)**
**Problem Type**:  
- Maximum/minimum sum/product of **k** consecutive elements.

**Approach**:  
1. Initialize pointers `L = 0` and `R = k-1`, calculating the initial window sum.  
2. Slide the window:  
   - Remove `arr[L]` from sum.  
   - Move `L` & `R` forward.  
   - Add `arr[R]` to sum.  



**Code Snippet**:
```python
def max_sum_subarray(arr, k):
    if len(arr) < k:
        return 0  # Or handle as appropriate

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum

```
**Complexity**: **O(n)** time, **O(1)** space.

---

### **Pattern 2: Longest Subarray/Substring With Condition**
**Problem Type**:  
- Finding the **longest valid** subarray where `sum ≤ K` (or other conditions).  

**Brute Force** (O(n²)) → **Optimal Sliding Window** (O(n)):  
- Expand window (`R++`) while valid (`sum ≤ K`).  
- Shrink (`L++`) if `sum > K`.  

**Optimization Insight**:  
- **Avoid shrinking excessively**: Instead of reducing window size to `1`, maintain `max_len` and only shrink minimally.  

**Code Snippet**:
```python
def longest_subarray(arr, K):
    L = 0
    max_len = 0
    total = 0

    for R in range(len(arr)):
        total += arr[R]
        while total > K:
            total -= arr[L]
            L += 1
        max_len = max(max_len, R - L + 1)

    return max_len

```
**Complexity**: **O(n)** per pointer pass (**~O(2n)** worst case, but optimized to O(n)).  

---

### **Pattern 3: Counting Subarrays With a Condition**
**Problem Type**:  
- Find **number of subarrays** where `sum = K` (or other comparisons).  

**Optimization Trick**:  
1. Compute subarrays with `sum ≤ K` (`count1`).  
2. Compute subarrays with `sum ≤ (K - 1)` (`count2`).  
3. Result: `count1 - count2`.  

**Example**:  
- For `sum = 4`: Count `sum ≤ 4` minus `sum ≤ 3`.  

**Code Snippet**:
```python
def subarrays_with_sum_lte(arr, K):
    count = 0
    L = 0
    total = 0

    for R in range(len(arr)):
        total += arr[R]
        while total > K:
            total -= arr[L]
            L += 1
        count += R - L + 1
    return count

def count_subarrays(arr, K):
    return subarrays_with_sum_lte(arr, K) - subarrays_with_sum_lte(arr, K - 1)

```
**Complexity**: **O(n)** per pass.

---

### **Pattern 4: Shortest/Minimum Valid Window**
**Problem Type**:  
- Find the **smallest subarray** where `sum ≥ K` (or meets a condition).  

**Approach**:  
1. Expand (`R++`) until condition met (`sum ≥ K`).  
2. Shrink (`L++`) to find minimal valid window.  

**Code Snippet**:
```python
def min_subarray_length(arr, K):
    L = 0
    total = 0
    min_len = float('inf')

    for R in range(len(arr)):
        total += arr[R]
        while total >= K:
            min_len = min(min_len, R - L + 1)
            total -= arr[L]
            L += 1

    return 0 if min_len == float('inf') else min_len

```
**Complexity**: **O(n)**.

---

## **3. Key Insights & Optimization**
1. **Shrinking Minimally** → Avoid unnecessary `L` movements, reducing time complexity.  
2. **Sliding Window vs Two-Pointer**:  
   - Sliding window: **Variable/fixed-size window** (subarrays).  
   - Two-pointer: **Fixed-direction movement** (e.g., sorted array pair sum).  
3. **Edge Cases**: Negative numbers, single-element subarrays, empty input.  

---

## **4. Practice Problems**
✅ **Fixed Window**: Maximum subarray sum of size `k`.  
✅ **Longest Substring with At Most K Distinct Characters**.  
✅ **Subarray Sum Equals K** (HashMap variant).  
✅ **Minimum Size Subarray Sum** (smallest window `≥` target).  

---
## **Further Reading**
🔗 **LeetCode Tags**: "Sliding Window," "Two Pointers"  
🔗 **Books**: *Algorithm Design Manual (Skiena), Elements of Programming Interviews (Aziz)*  

**[End of Notebook]**  

Would you like any sections expanded (e.g., more code examples, mathematical derivations)? # **Two-Pointer & Sliding Window Techniques**  
### *A Comprehensive Guide for Problem Solving*

---

## **1. Introduction**
The **two-pointer** and **sliding window** techniques are powerful problem-solving strategies in programming and algorithmic interviews. They allow efficient traversal and manipulation of arrays, strings, and other sequences. Unlike memorizing specific algorithms, these methods require understanding **how to dynamically adjust pointers/windows** based on conditions.

### **Key Takeaways**
✔ **Not memorization-based**—depends on pattern recognition & adaptability.  
✔ Enhances **time complexity** from brute-force (O(n²)) to optimized (O(n)).  
✔ Used in **arrays**, **strings**, **linked lists**, and **subarray/substring problems**.  

---

## **2. Four Problem Patterns**
Four common patterns where these techniques are applied:

### **Pattern 1: Constant-Size Window (Fixed-Length Subarrays)**
**Problem Type**:  
- Maximum/minimum sum/product of **k** consecutive elements.

**Approach**:  
1. Initialize pointers `L = 0` and `R = k-1`, calculating the initial window sum.  
2. Slide the window:  
   - Remove `arr[L]` from sum.  
   - Move `L` & `R` forward.  
   - Add `arr[R]` to sum.  

**Code Snippet**:
```javascript
function maxSumSubarray(arr, k) {
    let maxSum = 0, windowSum = 0;
    for (let i = 0; i < k; i++) windowSum += arr[i];  
    maxSum = windowSum;  
    for (let i = k; i < arr.length; i++) {  
        windowSum = windowSum - arr[i - k] + arr[i];  
        maxSum = Math.max(maxSum, windowSum);  
    }  
    return maxSum;  
}
```
**Complexity**: **O(n)** time, **O(1)** space.

---

### **Pattern 2: Longest Subarray/Substring With Condition**
**Problem Type**:  
- Finding the **longest valid** subarray where `sum ≤ K` (or other conditions).  

**Brute Force** (O(n²)) → **Optimal Sliding Window** (O(n)):  
- Expand window (`R++`) while valid (`sum ≤ K`).  
- Shrink (`L++`) if `sum > K`.  

**Optimization Insight**:  
- **Avoid shrinking excessively**: Instead of reducing window size to `1`, maintain `max_len` and only shrink minimally.  

**Code Snippet**:
```javascript
function longestSubarray(arr, K) {
    let L = 0, R = 0, max_len = 0, sum = 0;
    while (R < arr.length) {
        sum += arr[R];
        while (sum > K) {  // Shrink until valid
            sum -= arr[L];
            L++;
        }
        if (sum <= K) max_len = Math.max(max_len, R - L + 1);
        R++;
    }
    return max_len;
}
```
**Complexity**: **O(n)** per pointer pass (**~O(2n)** worst case, but optimized to O(n)).  

---

### **Pattern 3: Counting Subarrays With a Condition**
**Problem Type**:  
- Find **number of subarrays** where `sum = K` (or other comparisons).  

**Optimization Trick**:  
1. Compute subarrays with `sum ≤ K` (`count1`).  
2. Compute subarrays with `sum ≤ (K - 1)` (`count2`).  
3. Result: `count1 - count2`.  

**Example**:  
- For `sum = 4`: Count `sum ≤ 4` minus `sum ≤ 3`.  

**Code Snippet**:
```javascript
function countSubarrays(arr, K) {
    return subarraysWithSumLTE(arr, K) - subarraysWithSumLTE(arr, K - 1);
}
```
**Complexity**: **O(n)** per pass.

---

### **Pattern 4: Shortest/Minimum Valid Window**
**Problem Type**:  
- Find the **smallest subarray** where `sum ≥ K` (or meets a condition).  

**Approach**:  
1. Expand (`R++`) until condition met (`sum ≥ K`).  
2. Shrink (`L++`) to find minimal valid window.  

**Code Snippet**:
```javascript
function minSubarrayLength(arr, K) {
    let L = 0, min_len = Infinity, sum = 0;
    for (let R = 0; R < arr.length; R++) {
        sum += arr[R];
        while (sum >= K) {  // Shrink to minimize
            min_len = Math.min(min_len, R - L + 1);
            sum -= arr[L];
            L++;
        }
    }
    return min_len === Infinity ? 0 : min_len;
}
```
**Complexity**: **O(n)**.

---

## **3. Key Insights & Optimization**
1. **Shrinking Minimally** → Avoid unnecessary `L` movements, reducing time complexity.  
2. **Sliding Window vs Two-Pointer**:  
   - Sliding window: **Variable/fixed-size window** (subarrays).  
   - Two-pointer: **Fixed-direction movement** (e.g., sorted array pair sum).  
3. **Edge Cases**: Negative numbers, single-element subarrays, empty input.  

---

## **4. Practice Problems**
✅ **Fixed Window**: Maximum subarray sum of size `k`.  
✅ **Longest Substring with At Most K Distinct Characters**.  
✅ **Subarray Sum Equals K** (HashMap variant).  
✅ **Minimum Size Subarray Sum** (smallest window `≥` target).  

---
## **Further Reading**
🔗 **LeetCode Tags**: "Sliding Window," "Two Pointers"  
🔗 **Books**: *Algorithm Design Manual (Skiena), Elements of Programming Interviews (Aziz)*  

**[End of Notebook]**  
