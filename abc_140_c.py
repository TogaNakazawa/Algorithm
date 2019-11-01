n = int(input())
b_integers = list(map(int, input().split()))

a_integers = [b_integers[0]]
for i in range(n-2):
    if b_integers[i] > b_integers[i+1]:
        a_integers.append(b_integers[i+1])
    else:
        a_integers.append(b_integers[i])
a_integers.append(b_integers[-1])
print(sum(a_integers))
