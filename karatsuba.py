import math

def multiply(n1: str, n2: str) -> str:
    l1 = len(n1)
    l2 = len(n2)
    if l1 == 1 or l2 == 1:
        return str(int(n1) * int(n2))
    if l1 > l2:
        n2 = n2.rjust(len(n1), "0")
    if l2 > l1:
        n1 = n1.rjust(len(n2), "0")
    size = len(n1)
    m2 = size // 2
    a = n1[:m2]
    b = n1[m2:]
    c = n2[:m2]
    d = n2[m2:]
    ac = multiply(a, c)
    bd = multiply(b, d)
    abcd = multiply(add(a, b), add(c, d))
    exp = size - m2
    z2 = ac + (2*exp)*"0"
    z1 = str(int(abcd) - int(ac) - int(bd)) + exp*"0"
    z0 = bd
    return str(int(z2) + int(z1) + int(z0))

def add(n1, n2):
    return str(int(n1) + int(n2))

x = "3141592653589793238462643383279502884197169399375105820974944592"
y = "2718281828459045235360287471352662497757247093699959574966967627"
print(multiply(x, y))
print(int(x)*int(y))