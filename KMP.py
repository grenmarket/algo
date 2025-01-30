def prefix_table(s):
    pref = [0]
    k = 0
    for n in range(1, len(s)):
        while k > 0 and s[k] != s[n]:
            k = pref[k-1]
        if s[k] == s[n]:
            k += 1
        pref.append(k)
    return pref


def kmp(text, pattern):
    k = 0
    pt = prefix_table(pattern)
    for n in range(0, len(text)):
        while k > 0 and pattern[k] != text[n]:
            k = pt[k-1]
        if pattern[k] == text[n]:
            k += 1
        if k == len(pattern):
            print(str(n - k))
            k = pt[k-1]
