def repeating_without_characters (s : str):
    l = 0 
    r = 0 
    maxlen = 0 
    setx = set()
    for r in range(len(s)):
        while s[r] in setx:
            setx.remove(s[l])
            l+= 1 
        setx.add(s[r])
        maxlen = max(maxlen, r - l + 1)
    return maxlen
    
s = "abcabdaecbd"
print(repeating_without_characters(s))
