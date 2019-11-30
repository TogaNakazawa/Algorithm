a,b = map(int,input().split())
import fractions
import collections
import copy
def prime_factorization(n):
    a = [1]
    n1 = copy.deepcopy(n)
    while n % 2 == 0:
        n //= 2
    if n1 != n:
        a.append(2)
    f = 3
    while f * f <= n:
        if n % f == 0:
            n //= f
            if a[-1] != f:
                a.append(f)
        else:
            f += 2
    if a[-1] != n and n != 1:
        a.append(n)
    return a
print(len(prime_factorization(fractions.gcd(a,b))))
