## 'aabbccddaaa'

from collections import defaultdict

def longest_substring_with_k_characters (s: str, k):
    max_len = 0
    
    for i in range(len(s)):
        counter = defaultdict(int)
        for j in range(i, len(s)):
            counter[s[j]] += 1 
            
            if len(counter) > k:
                break 
            max_len = max(max_len, j - i + 1)
    return max_len

s = 'aabbccddaaa'
k = 2 
print(longest_substring_with_k_characters(s, k))
