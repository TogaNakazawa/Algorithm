h, w, a, b = map(int, input().split())
list = []

def return_duplicate_permutation(h_or_w, a_or_b):
    x = 1
    y = 1
    z = 1
    for i in range(1, h_or_w+1):
        x *= i
    for i in range(1, a_or_b+1):
        y *= i
    for i in range(1, h_or_w - a_or_b + 1):
        z *= i
    num = x / (y * z)
    return num

if h < 2 * a or w < 2 * b:
    print("No")
elif a is 0 and b is not 0:
    print("No")
elif a is not 0 and b is 0:
    print("No")
elif a is 0 and  b is 0:
    for i in range(w):
        temp = ["0"] * h
        print(temp.join(""))
else:
    num = return_duplicate_permutation(h,a)
    if w % num == 0:
        slice = int(w // num)
        for l in range(slice):
            for i in range(w):
                temp = ["1"] * h
                for p in range(i,i+a):
                    temp[p] = 0
                print((" ").join(map(str,temp)))
    else:
        print("No")
