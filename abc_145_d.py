a,b = map(int, input().split())
tried = (a + b)//3
imf = 10**9 +7
import itertools
if a < tried or b < tried or (a+b)%3 != 0:
    print(0)
    quit()
if abs(a-b) == 0:
    one = tried//2
else:
    one = abs(a-b)
import itertools
# def kaijo(n):
#     ans = 1
#     counter = 0
#     for i in range(1,n+1):
#         ans *= i
#         if ans > 10**9 + 7:
#             ans = ans % (10**9 + 7)
#         counter += 1
#     counter = 0
#     return ans
ans = len(list(itertools.combinations(range(tried), one)))//imf
print(ans)
