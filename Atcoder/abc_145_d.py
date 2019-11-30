a,b = map(int, input().split())
tried = (a + b)//3
p = 10**9 +7

if a < tried or b < tried or (a+b)%3 != 0:
    print(0)
    quit()
one = int((2 * a -  b)/3)
n = tried
r = min(one, tried-one)
n_fac = 1
r_fac = 1
n_r_fac = 1

for i in range(2,n+1):
    n_fac *= i
    n_fac %= p
for i in range(2,r+1):
    r_fac *= i
    r_fac %= p
for i in range(2,n-r+1):
    n_r_fac *= i
    n_r_fac %= p
r_fac_inverse = pow(r_fac, p-2, p)
n_r_fac_inverse = pow(n_r_fac, p-2, p)

print((n_fac * r_fac_inverse * n_r_fac_inverse)%p)
