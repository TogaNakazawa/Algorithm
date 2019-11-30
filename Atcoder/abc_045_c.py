n = list(input())
gaps = len(n) - 1
import copy
ans = 0
for i in range(2 ** gaps):
    formula = copy.deepcopy(n)
    ops = [""] * gaps
    for j in range(gaps):
        if (i >> j) & 1:
            ops[gaps-j-1] = "+"
    formula1 = ""
    for f,op in zip(formula,ops + [""]):
        formula1 += (str(f) + op)
    ans += eval(formula1)
print(ans)
