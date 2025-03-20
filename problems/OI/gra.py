import sys

def consecutive(a, b, c, n_mod):
    abc_sorted = [a,b,c]
    abc_sorted.sort()
    if (abc_sorted[1] == (abc_sorted[0] + 1) % n_mod) and (abc_sorted[2] == (abc_sorted[1] + 1) % n_mod):
        return True
    if (abc_sorted[1] == (abc_sorted[0] + 1) % n_mod) and (abc_sorted[0] == (abc_sorted[2] + 1) % n_mod):
        return True
    if (abc_sorted[0] == (abc_sorted[2] + 1) % n_mod) and (abc_sorted[2] == (abc_sorted[1] + 1) % n_mod):
        return True
    return False

n = int(input())
black = [int(item) for item in input().split()]
are_consecutive = consecutive(*black, n)
# should be n % 2 == 1
if are_consecutive or n % 2 == 0:
    sys.stdout.write('TAK')
else:
    sys.stdout.write('NIE')