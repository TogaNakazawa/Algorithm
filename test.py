n = int(input())
vertex_list = list(map(int, input().split()))
vertex_list.sort()
ans = 1
mark = 0
if vertex_list[0] != 0:
    print(0)
else:
    maxx = vertex_list[-1]
    for i in range(1,n):
        if vertex_list[i] is not 0 and vertex_list[1]-vertex_list[i-1]<2:
            ans *= vertex_list[i]
        else:
            mark =  1
    if mark == 0:
        print(ans)
    else:
        print(0)
