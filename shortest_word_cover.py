def prefix_suffix_table(s, i):
    if i == 0:
        return [0]
    prev = prefix_suffix_table(s, i - 1)
    if s[i] == s[prev[-1]]:
        prev.append(prev[-1] + 1)
    else:
        prev.append(0 if s[i] != s[0] else 1)
    return prev


def shortest_cover(word):
    # easier to operate on 1-indexed arrays
    ps_table = [0] + prefix_suffix_table(word, len(word)-1)
    cover_range = [i for i in range(0, len(word)+1)]
    cover = cover_range.copy()
    for i in range(2, len(word)+1):
        # ps_table[i] is the longest prefix-suffix of word[1...i]
        # cover[longest prefix-suffix of k] is the shortest cover of that prefix-suffix
        # cover_range[cover of prefix-suffix of k] is the length of the longest part of word[1...i] that can be
        # covered with that cover

        # if the word V is a prefix-suffix of the word X, and the word W is a cover of the word X (and |W| <= |V|)
        # then W is also a cover of V
        if ps_table[i] > 0 and i - cover_range[cover[ps_table[i]]] <= cover[ps_table[i]]:
            cover[i] = cover[ps_table[i]]
            cover_range[cover[ps_table[i]]] = i
    return word[:cover[ps_table[-1]]]

print(shortest_cover('ababbababbabababbabababbababbaba'))
# ababbababbabababbabababbababbaba
# ababbaba
#      ababbaba
#             ababbaba
#                    ababbaba
#                         ababbaba
