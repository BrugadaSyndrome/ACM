import sys
import math

def main():
    line_count = int(sys.stdin.readline().strip())

    for i in range(line_count):
        num = int(sys.stdin.readline().strip())
        print math.factorial(num)

main()
