import sys


# 5! 5*4*3*2*1
def factorial(num):
    # base case
    if (num == 1): return 1
    # recursive case
    return num * factorial(num - 1)


in_num = int(sys.argv[1])
result = factorial(in_num)

# display the results
print("%d!= %d" % (in_num, result))
