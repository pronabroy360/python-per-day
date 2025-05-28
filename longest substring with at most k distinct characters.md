Here's a **very detailed guidebook** based on the transcript above that explains how to solve the **"Longest Substring with At Most K Distinct Characters"** problem using various approaches including brute force, optimized sliding window, and further refinement to achieve optimal time complexity.

---

# 📘 Guidebook: Longest Substring with At Most K Distinct Characters

---

## 🧠 Problem Understanding

### 🔹 Problem Statement

* You are given:

  * A **string** `s`
  * An **integer** `k`

* Your task:

  * Find the **length** of the **longest substring** of `s` that contains **at most `k` distinct characters**.

### 🔹 Definitions

* **Substring**: A contiguous sequence of characters within the string.

  * Example: `"abcde"` has substrings like `"abc"`, `"cde"`, `"bcd"`.

* **Distinct Characters**: Characters that are different from each other.

  * `"aabc"` has 3 distinct characters: `a, b, c`.

---

## 🐢 Brute Force Approach

### 🔹 Idea

* Generate **all substrings** of `s`.
* For each substring:

  * Count the number of distinct characters.
  * If it has ≤ `k` distinct characters:

    * Update the max length if it's the longest so far.

### 🔹 Pseudocode

```python
def longest_substring_k_distinct_brute(s, k):
    max_len = 0
    n = len(s)
    
    for i in range(n):
        char_map = {}
        for j in range(i, n):
            char_map[s[j]] = char_map.get(s[j], 0) + 1
            if len(char_map) <= k:
                max_len = max(max_len, j - i + 1)
            else:
                break
    return max_len
```

### 🔹 Complexity

* **Time**: O(n²)
* **Space**: O(256) → Max possible distinct ASCII characters.

---

## ⚡ Sliding Window with Two Pointers (Optimized)

### 🔹 Idea

Use a **sliding window** with two pointers `l` and `r` and a **hash map** to track character frequencies.

* Expand the window by moving `r` (right pointer).
* If distinct characters > `k`, shrink the window by moving `l` (left pointer).
* Track the **maximum window size** where the condition holds.

### 🔹 Steps

1. Initialize:

   * `l = 0, r = 0`
   * `max_len = 0`
   * `char_map = {}`

2. While `r < len(s)`:

   * Add `s[r]` to `char_map`
   * If `char_map` size > `k`:

     * Shrink the window by moving `l` and updating `char_map`
     * Remove character if its count drops to 0
   * Update `max_len = max(max_len, r - l + 1)`
   * Move `r` forward

### 🔹 Pseudocode

```python
def longest_substring_k_distinct(s, k):
    from collections import defaultdict
    
    l = 0
    max_len = 0
    char_map = defaultdict(int)

    for r in range(len(s)):
        char_map[s[r]] += 1

        while len(char_map) > k:
            char_map[s[l]] -= 1
            if char_map[s[l]] == 0:
                del char_map[s[l]]
            l += 1

        max_len = max(max_len, r - l + 1)
    
    return max_len
```

### 🔹 Complexity

* **Time**: O(n)

  * Each character is visited at most twice (once by `r`, once by `l`).
* **Space**: O(k) or O(256) depending on character set.

---

## 🏆 Most Optimized Version (Avoid Trimming Too Much)

### 🔹 Idea

In the previous version, when the distinct character count exceeds `k`, we **trim** the window **until** the substring becomes valid. This may unnecessarily reduce the window length too much.

Instead:

* Remove **one character at a time** from the left
* **Always preserve** the largest valid window as long as possible

### 🔹 Advantages

* Prevents the window from reducing in size more than needed
* Allows **next valid window** to directly extend from the longest previous valid one

### 🔹 Pseudocode (Refined)

```python
def longest_substring_k_distinct_optimized(s, k):
    from collections import defaultdict
    
    l = 0
    max_len = 0
    char_map = defaultdict(int)

    for r in range(len(s)):
        char_map[s[r]] += 1

        if len(char_map) > k:
            char_map[s[l]] -= 1
            if char_map[s[l]] == 0:
                del char_map[s[l]]
            l += 1

        max_len = max(max_len, r - l + 1)

    return max_len
```

> ✅ This version achieves **true O(n)** performance.

---

## 🧮 Time & Space Complexity Summary

| Approach              | Time Complexity | Space Complexity |
| --------------------- | --------------- | ---------------- |
| Brute Force           | O(n²)           | O(256)           |
| Sliding Window        | O(n)            | O(256)           |
| Optimized SW (Trim 1) | O(n)            | O(256)           |

---

## 💡 Example Walkthrough

Let’s run through an example:

```python
s = "aabbaaccdd"
k = 2
```

* Sliding window tracks longest substring with ≤ 2 distinct chars.
* Valid substrings:

  * `"aabba"` → Length 5
  * `"bbaacc"` → Length 6
* Final answer: **6**

---

## 🛠️ Template Summary for Interviews

### Sliding Window Template (Most Efficient)

```python
def longest_substring_k_distinct(s, k):
    from collections import defaultdict
    l = 0
    max_len = 0
    freq_map = defaultdict(int)

    for r in range(len(s)):
        freq_map[s[r]] += 1

        while len(freq_map) > k:
            freq_map[s[l]] -= 1
            if freq_map[s[l]] == 0:
                del freq_map[s[l]]
            l += 1

        max_len = max(max_len, r - l + 1)
    
    return max_len
```

---

## 🧑‍💻 Tips for Interviews

* Start by **explaining the brute force** to show understanding.
* Mention **time complexity** early.
* Propose **sliding window** as optimization.
* Highlight **why it's O(n)**.
* If asked to optimize further, discuss **"trimming one step" vs "full valid window shrinking"**.

---

## ✅ Final Thoughts

* The sliding window + hashmap is a **powerful combo** for substring problems.
* This pattern also applies to:

  * Longest substring without repeating characters
  * Longest substring with exactly K distinct characters

---

Would you like this turned into a downloadable PDF or used as a cheat sheet?
