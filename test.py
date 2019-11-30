a,b,x = map(int,input().split())

def price(n):
    return int(a * n + b * len(str(n)))

def bisect(start,end):
    if abs(start-end) <= 1:
        if price(end) <= x:
            return end
        else:
            return start
    else:
        middle = (start + end) // 2
        if price(middle) <= x:
            return bisect(middle,end)
        else:
            return bisect(start,middle)

print(bisect(0,10**9))
