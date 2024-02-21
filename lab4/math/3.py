import math
n = int(input())
l = int(input())
a = l/(2*(math.tan(math.pi/n)))
s = int(l*n*a/2)
print(s)