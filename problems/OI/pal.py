def _min_palindrome(word):
    forward = ''
    backwards = ''
    indexes_of_palindromes = []
    for i in range(2, len(word)+1, 2):
        slice = word[i-2:i]
        forward += slice
        backwards = slice[::-1] + backwards
        if forward == backwards:
            forward = ''
            backwards = ''
            indexes_of_palindromes.append(i)
    return indexes_of_palindromes

b = 'bbaabbaabbbaaaaaaaaaaaabbbaa'
print(len(b))
print(_min_palindrome(b))
print([len(b) - n for n in _min_palindrome(b[::-1])])