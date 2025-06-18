Great work! You're approaching the **Maximum Subarray Sum** problem progressively — from brute force to optimal. Let's go through the **complete journey**, from **intuition → optimization**, step-by-step.

---

## ✅ Problem Statement

> Given an array of integers (can include negatives), find the **maximum possible sum of a contiguous subarray**.

Example:
`[-1, 5, -4, 2, 3, 1, -10, 2]` → Maximum subarray sum = `7` (from `[5, -4, 2, 3, 1]`)

---

## 🧠 Step-by-Step Approach & Intuition

---

### 🔴 1. **Brute Force** (Time: O(n³))

#### Code:

```python
for i in range(len(arr)):
    for j in range(i, len(arr)):
        Sum = 0
        for k in range(i, j+1):
            Sum += arr[k]
            maximum = max(maximum, Sum)
```

#### Intuition:

* Try **every possible subarray**.
* For each subarray (i to j), calculate sum by iterating from i to j.
* Keep track of maximum sum encountered.

#### Why it's slow:

* 3 nested loops: `i`, `j`, and `k` → **O(n³)** time.
* Not scalable for large inputs.

---

### 🟠 2. **Better Brute Force with Prefix-like Optimization** (Time: O(n²))

#### Code:

```python
for i in range(len(arr)):
    Sum = 0
    for j in range(i, len(arr)):
        Sum += arr[j]
        maximum = max(maximum, Sum)
```

#### Intuition:

* Same as brute force, but avoid recalculating subarray sum from scratch.
* Maintain running sum in inner loop:

  * If you're at `i` and going to `j`, just add `arr[j]` to the previous sum.

#### Why it's better:

* Removed innermost loop → now just two loops → **O(n²)**.
* Still slow for very large arrays but significantly faster than O(n³).

---

### 🟢 3. **Optimal: Kadane’s Algorithm** (Time: O(n))

#### Code:

```python
maximum = -∞
Sum = 0
for i in range(len(arr)):
    Sum += arr[i]
    maximum = max(maximum, Sum)
    if Sum < 0:
        Sum = 0
```

#### Intuition:

* We don’t need to explicitly consider every subarray.
* At each element, ask:

  * "Should I **extend** the previous subarray, or **start fresh** from here?"
* If running sum becomes negative, **it won’t help future subarrays**, so we reset it.

#### Real insight:

* We're simulating all subarrays *ending at index i* using just a running variable.
* It's a **greedy + dynamic programming** hybrid.

#### Why it works:

* We maintain the best sum ending at current index.
* Whenever running sum drops below 0, we reset, as continuing would hurt future sums.

#### Time:

* Only one pass → **O(n)**
* Space: **O(1)** (no extra space needed)

---

## 🧮 Dry Run Example

Array: `[-1, 5, -4, 2, 3, 1, -10, 2]`

| i | arr\[i] | Sum                   | max\_so\_far |
| - | ------- | --------------------- | ------------ |
| 0 | -1      | -1 → reset 0          | -1           |
| 1 | 5       | 0 + 5 = 5             | 5            |
| 2 | -4      | 5 - 4 = 1             | 5            |
| 3 | 2       | 1 + 2 = 3             | 5            |
| 4 | 3       | 3 + 3 = 6             | 6            |
| 5 | 1       | 6 + 1 = 7             | 7 ✅          |
| 6 | -10     | 7 - 10 = -3 → reset 0 | 7            |
| 7 | 2       | 0 + 2 = 2             | 7            |

Final Answer: `7`

---

## 🧠 Summary Table

| Approach     | Time Complexity | Space | Description                                |
| ------------ | --------------- | ----- | ------------------------------------------ |
| Brute Force  | O(n³)           | O(1)  | Try all subarrays, sum them manually       |
| Better Brute | O(n²)           | O(1)  | Running sum in inner loop                  |
| Kadane's     | O(n)            | O(1)  | Smart dynamic greedy decision at each step |

---

## ✅ Final Thoughts:

* Kadane’s Algorithm is a must-know for interviews and DSA — it's elegant, optimal, and teaches key algorithmic patterns.
* You **don’t need sliding window** here, because the subarray size is unknown and variable.
* Progressing from brute force → optimization builds strong problem-solving intuition.

Let me know if you want to visualize this using a graph, or want to see the **subarray itself**, not just the sum.
