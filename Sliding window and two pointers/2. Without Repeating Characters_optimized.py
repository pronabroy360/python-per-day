def without_replacing_characters(s: str):
    l = 0
    r = 0 
    max_len = 0
    
    if len(s) == 0:
        return 0
    
    setx = set()
    
    for r in range(len(s)):
        while s[r] in setx:
            setx.remove(s[l])                            #once did mistake replacing r as l.
            l += 1 
        setx.add(s[r])
        
        max_len = max(max_len, r - l+1)
    return max_len

if __name__ == "__main__":
    s = "abcabdcef"
    print(without_replacing_characters(s))
