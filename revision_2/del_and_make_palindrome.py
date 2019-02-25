def palindromeIndex(s):
    if s == s[::-1]:
        return -1
    i = 0
    while i < len(s):
        ss = s[:i] + s[i+1:]
        if ss == ss[::-1]:
            return i
        i = i + 1
    return -1



print(palindromeIndex("qdbab"))