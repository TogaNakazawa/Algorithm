<<<<<<< HEAD
w,h,x,y = map(int,input().split())

midpoint = [w/2, h/2]
=======
n = list(input())
gaps = (len(n) - 1) * ["-"]
for i in range(2 ** len(gaps)):
    for j in range(len(gaps)):
        if (i>>j) & 1:
            gaps[len(gaps) - j - 1] = "+"
    formula = ""
    for nn, gap in zip(n, gaps + [""]):
        formula += (nn + gap)
    result = eval(formula)
    if result == 7:
        print(formula + "=7")
        quit()
>>>>>>> c866ee59cdeef7f887f322343b9a96602e668036
