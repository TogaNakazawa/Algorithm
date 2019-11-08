a,b,c,d = map(int,input().split())
from fractions import gcd
lcm = c * d // gcd(c, d)
def num_of_complements(x,c,d,lcm):
    num = x + x//lcm - x//c - x//d
    return num

ans = num_of_complements(b,c,d,lcm) - num_of_complements(a-1,c,d,lcm)
print(ans)
