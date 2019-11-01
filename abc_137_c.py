n = int(input())
strings_list = [list(input()) for i in range(n)]
counter = 0
dict = {}

for strings in strings_list:
    strings = "".join(sorted(strings))
    if strings in dict.keys():
        counter += dict[strings]
        dict[strings] += 1
    else:
        dict[strings] = 1
print(counter)
