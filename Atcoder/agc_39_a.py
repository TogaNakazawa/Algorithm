strings = list(input())
k = int(input())
counter = 0
same_starts = 0
for  i in range(len(strings)-1):
    if strings[i] != strings[i+1]:
        break
    same_starts += 1
for  i in range(len(strings)-1):
    if strings[i] == strings[i+1]:
        strings[i+1] = str(counter)
        counter += 1

if strings[0] != strings[-1]:
    print(counter * k)
else:
    # 文字列が１種類の時
    if (same_starts + 1) == len(strings):
        # 文字列の個数が偶数の時
        if len(strings) % 2 == 0:
            print(k * len(strings)//2)
        else:
        # 文字列が奇数の時
            # 文字列を繰り返す回数が偶数回の時
            if k % 2 == 0:
                print(counter * k // 2 + (counter + 1) * k // 2)
            else:
            # 文字列を繰り返す回数が奇数回の時
                print(counter * ((k - 1) // 2 + 1)+ (counter + 1) * (k - 1)//2)
    else:
        if (same_starts+1) % 2 == 0:
            print(counter * k)
        else:
            print((counter+1) * (k-1) + counter)
