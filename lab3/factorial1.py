
import sys

# 5! = 5*4*3*2*1
def factorial(num):
    total = 1
    for i in range(1, num+1):
        total = total * i
    return total

# add checks here
in_num = int(sys.argv[1])
out_num = factorial(in_num)

# display results
print("%d! = %d" % (in_num, out_num))