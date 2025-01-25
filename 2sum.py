def init():
    nums = set()
    with open('files/2sum.txt', 'r') as file:
        for line in file:
            nums.add(int(line.strip()))
    return nums

nums = init()

grouped = {}
for n in nums:
    key = abs(n)//10000
    if key not in grouped:
        grouped[key] = set()
    grouped[key].add(n)

sums = set()
for n in nums:
    key = abs(n) // 10000
    joined = grouped.get(key-1, set()) | grouped.get(key, set()) | grouped.get(key+1, set())
    for x in joined:
        sum = x+n
        if x != n and abs(sum) <= 10000:
            sums.add(sum)
print(len(sums))