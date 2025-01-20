from collections import Counter

a = [4,6,5,3,4,4,4,5,5,6,6,7,8,8,8,7]
freq = Counter(a)
print(dict(sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]))