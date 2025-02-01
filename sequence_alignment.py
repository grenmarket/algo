def max_alignment(a: str, b: str, gap_penalty, mismatch_penalty):
    result = [[0] * (len(a)+1) for _ in range(len(b)+1)]
    for i in range(len(a)+1):
        result[0][i] = i * gap_penalty
    for j in range(len(b)+1):
        result[j][0] = j * gap_penalty
    for i in range(len(a)):
        for j in range(len(b)):
            char_i = a[i]
            char_j = b[j]
            m_penalty = mismatch_penalty if char_j != char_i else 0
            result[j+1][i+1] = min([
                m_penalty + result[j][i],
                gap_penalty + result[j][i+1],
                gap_penalty + result[j+1][i]
            ])
    min_penalty = result[-1][-1]
    s1, s2 = reconstruct(result, a, b, mismatch_penalty, gap_penalty)
    return min_penalty, s1, s2

def reconstruct(result, a: str, b: str, mismatch_penalty, gap_penalty):
    i = -1
    j = -1
    penalty = result[j][i]
    s1 = ''
    s2 = ''
    while penalty > 0:
        m_penalty = mismatch_penalty if b[j] != a[i] else 0
        case_1 = result[j-1][i-1] + m_penalty
        case_2 = result[j-1][i] + gap_penalty
        case_3 = result[j][i-1] + gap_penalty
        min_penalty = min([case_3, case_2, case_1])
        if case_1 == min_penalty:
            s1 += a[i]
            s2 += b[j]
            i -= 1
            j -= 1
            penalty -= m_penalty
        elif case_2 == min_penalty:
            s1 += '_'
            s2 += b[j]
            j -= 1
            penalty -= gap_penalty
        elif case_3 == min_penalty:
            s1 += a[i]
            s2 += '_'
            i -= 1
            penalty -= gap_penalty
    s1 += a[i::-1]
    s2 += b[j::-1]
    return s1[-1::-1], s2[-1::-1]


s1 = 'ACCCGA'
s2 = 'ACTA'
print(max_alignment(s1, s2, 1, 3))