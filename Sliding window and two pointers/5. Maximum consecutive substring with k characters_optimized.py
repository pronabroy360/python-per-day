from collections import defaultdict 

def with_k_character_replacement (s: str, k):
    if len(s) == 0:
        return 0 
    
    l = 0 
    r = 0 
    max_len = 0 
    counter = defaultdict(int)
    
    for r in range(len(s)):
        counter[s[r]] += 1 
        
        while len(counter) > k:
            counter[s[l]] -= 1 
            
            if counter[s[l]] == 0:
                del counter[s[l]]
            l += 1
        max_len = max(max_len, r - l + 1)
    return max_len

s = 'aabbccddaaa'
k = 2 
print(with_k_character_replacement(s, k))
