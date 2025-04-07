import sys

ceiling = 2_000_000_000
primes = [2,3,5,7,11,13,17,19,23,29]
# precomputed using generate_anti_primes
anti_primes = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260, 1680, 2520, 5040, 7560, 10080, 15120, 20160, 25200, 27720, 45360, 50400, 55440, 83160, 110880, 166320, 221760, 277200, 332640, 498960, 554400, 665280, 720720, 1081080, 1441440, 2162160, 2882880, 3603600, 4324320, 6486480, 7207200, 8648640, 10810800, 14414400, 17297280, 21621600, 32432400, 36756720, 43243200, 61261200, 73513440, 110270160, 122522400, 147026880, 183783600, 245044800, 294053760, 367567200, 551350800, 698377680, 735134400, 1102701600, 1396755360]

def init():
    number = int(input())
    for i in range(1, len(anti_primes)):
        if anti_primes[i] > number:
            sys.stdout.write(str(anti_primes[i-1]))
            break


def generate_anti_primes():
    candidates = []
    _gen(candidates, 0, 31, 1, 1)
    candidates.sort(key=lambda item: item[0])
    result = []
    max_num_of_divisors = 0
    for c in candidates:
        num_of_divisors = c[1]
        if num_of_divisors > max_num_of_divisors:
            max_num_of_divisors = num_of_divisors
            result.append(c[0])
    return result



def _gen(candidates, prime_index, max_potential, candidate, num_of_divisors):
    candidates.append((candidate, num_of_divisors))
    for i in range(1, max_potential+1):
        if primes[prime_index] > ceiling // candidate:
            return
        candidate = candidate * primes[prime_index]
        _gen(candidates, prime_index+1, i, candidate, num_of_divisors * (i+1))

init()