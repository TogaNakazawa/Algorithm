li = list(input())
a = li.count("0")
import math
if a < math.ceil(len(li)/2):
    print(2*a)
else:
    print(2*(len(li)-a))
