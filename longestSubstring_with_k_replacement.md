
---

# 📘 Guidebook: Solving "Longest Repeating Character Replacement" Using Sliding Window & Two-Pointer Approach

---

## 📌 Problem Statement

You are given:

* A string `s` consisting of **uppercase English letters**.
* An integer `k`.

**Goal**: Find the **length of the longest substring** that can be formed where all characters are the **same**, after replacing **at most `k` characters** in the substring with any other uppercase letter.

---

## 🔍 Example

### Input:

```plaintext
s = "AABABBA"
k = 1
```

### Output:

```plaintext
4
```

### Explanation:

* Replace the second 'B' with 'A' → "AABAABA" → substring "AABA" → 3 'A's and 1 replaced.
* Longest such possible substring = 4.

---

## 🚀 Brute Force Approach

### Step-by-Step:

1. **Generate all substrings** of `s`.
2. For each substring, count the **frequency of characters**.
3. Determine **how many characters need to be changed** to make the substring all the same.
4. If changes ≤ `k`, update the answer with this substring's length.

### Key Insight:

To make all characters the same:

```plaintext
Changes needed = (Length of substring) - (Max frequency of any character in the substring)
```

---

### 🔢 Brute Force Pseudocode:

```python
max_len = 0
for i in range(len(s)):
    freq = [0]*26
    max_freq = 0
    for j in range(i, len(s)):
        freq[ord(s[j]) - ord('A')] += 1
        max_freq = max(max_freq, freq[ord(s[j]) - ord('A')])
        if (j - i + 1) - max_freq <= k:
            max_len = max(max_len, j - i + 1)
```

### Time Complexity:

* O(N²) due to the nested loops.
* Space: O(26) = O(1) constant, as only 26 characters are tracked.

---

## ⚙️ Optimized Approach: Sliding Window + Two Pointers

### Core Idea:

Use a **sliding window** (`left`, `right` pointers):

* Expand the window from the right.
* Keep track of character frequencies within the window.
* If the window becomes invalid (more than `k` changes needed), **shrink from the left**.

### ✅ Valid Window Condition:

```plaintext
Window length - Max frequency of a character in the window ≤ k
```

---

### ⚡ Optimized Algorithm Steps

1. Initialize:

   * `left = 0`, `max_len = 0`, `max_freq = 0`
   * Frequency array `freq = [0]*26`

2. Loop through the string using `right`:

   * Update frequency of `s[right]`
   * Update `max_freq` if needed
   * If the window is **invalid**, move `left` pointer forward
   * Update `max_len`

---

### 💡 Optimization Note:

Even if the `max_freq` is outdated after shrinking the window, we **don’t recalculate** it because:

* We’re only interested in finding longer valid substrings.
* A reduced `max_freq` won’t help achieve a longer substring.

---

### ✅ Final Optimized Code (Python):

```python
def characterReplacement(s: str, k: int) -> int:
    freq = [0] * 26
    left = 0
    max_freq = 0
    max_len = 0

    for right in range(len(s)):
        idx = ord(s[right]) - ord('A')
        freq[idx] += 1
        max_freq = max(max_freq, freq[idx])

        # Check if window is valid
        if (right - left + 1) - max_freq > k:
            freq[ord(s[left]) - ord('A')] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
```

---

## 🧠 Dry Run Example

Input: `s = "AABABBA"`, `k = 1`

| Step | Left | Right | Window  | MaxFreq | WindowLength - MaxFreq | Valid? | MaxLen |
| ---- | ---- | ----- | ------- | ------- | ---------------------- | ------ | ------ |
| 1    | 0    | 0     | "A"     | 1       | 0                      | ✅      | 1      |
| 2    | 0    | 1     | "AA"    | 2       | 0                      | ✅      | 2      |
| 3    | 0    | 2     | "AAB"   | 2       | 1                      | ✅      | 3      |
| 4    | 0    | 3     | "AABA"  | 3       | 1                      | ✅      | 4      |
| 5    | 0    | 4     | "AABAB" | 3       | 2                      | ❌      |        |
| 6    | 1    | 4     | "ABAB"  | 2       | 2                      | ❌      |        |
| 7    | 2    | 4     | "BAB"   | 2       | 1                      | ✅      |        |
| 8    | 2    | 5     | "BABB"  | 3       | 1                      | ✅      | 4      |

---

## 🧠 Time and Space Complexity

| Metric           | Value        |
| ---------------- | ------------ |
| Time Complexity  | O(N)         |
| Space Complexity | O(26) = O(1) |

---

## 🧰 Summary

| Approach       | Time Complexity | Space Complexity | Valid for Interview |
| -------------- | --------------- | ---------------- | ------------------- |
| Brute Force    | O(N²)           | O(1)             | ❌                   |
| Sliding Window | O(N)            | O(1)             | ✅                   |

---

## 🔖 Key Takeaways

* Use **sliding window** where dynamic window size is required.
* Always look for **max frequency character** to minimize replacements.
* Avoid recalculating frequency unnecessarily for performance.
* Great problem to **practice window validity checks**.

---


Would you like any of those additions?
