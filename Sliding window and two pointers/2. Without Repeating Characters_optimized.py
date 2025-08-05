def without_replacing_characters(s: str):
    l = 0
    r = 0 
    max_len = 0
    
    if len(s) == 0:
        return 0
    
    setx = set()
    
    for r in range(len(s)):
        if s[r] in setx:
            setx.remove(s[r])
            l += 1 
        setx.add(s[r])
        r += 1
        
        max_len = max(max_len, r - l)
    return max_len

if __name__ == "__main__":
    s = "abcabdcef"
    print(without_replacing_characters(s))
