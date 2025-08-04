def withoutRepeatingCharacters(s: str):
    if len(s) == 0:
        return 0 
    maxlen = 0

    for i in range(len(s)):
        setx = {}
        for j in range(i, len(s)):  # fix here: explore substrings starting at i
            if s[j] in setx:
                break
            setx[s[j]] = 1
            maxlen = max(maxlen, j - i + 1)  # fix: calculate substring length

    return maxlen

s = "aabcabcdebc"
print(withoutRepeatingCharacters(s))
