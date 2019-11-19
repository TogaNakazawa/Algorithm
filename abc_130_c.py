w,h,x,y = map(int,input().split())
midpoint = [w/2, h/2]

if [x,y] == midpoint:
    print(str(w*h/2) + " 1")
else:
    print(str(w*h/2) + " 0")
