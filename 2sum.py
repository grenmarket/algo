def init():
    nums = set()
    with open('files/2sum.txt', 'r') as file:
        for line in file:
            nums.add(int(line.strip()))
    return nums

nums = init()
result = 0
for i in range(-10000, 10001):
    print(i)
    for num in nums:
        complementary = i - num
        if complementary != num and complementary in nums:
            result += 1
            break
print(result)