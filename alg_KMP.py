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


print(prefix_table("aaabaaaab"))