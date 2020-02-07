import sys
import os

os.system('color')

print (u"\u001b[30m A \u001b[31m B \u001b[32m C \u001b[33m D \u001b[0m")
print (u"\u001b[34m E \u001b[35m F \u001b[36m G \u001b[37m H \u001b[0m")
'''
for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
    print (u"\u001b[0m")
'''

print("\033[38;5;38 TEXT  \033[0m")


def print_arr2D(arr):
    for line in arr:
        print(*line)
