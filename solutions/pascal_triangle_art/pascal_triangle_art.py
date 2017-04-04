import math
import sys

def pascal_num(row, pos):
    return ((math.factorial(row))/((math.factorial(pos))*(math.factorial(row-pos))))

def pascal_row(row_number):
    row = []
    for i in range(row_number+1):
        row.append(pascal_num(row_number, i))
    return row

def main():
    N = int(sys.stdin.readline().strip())
    M = int(sys.stdin.readline().strip())

    for i in range(N):
        line = ' '*(N-(i+1))

        row = pascal_row(i)

        for r in row:
            if (r % M != 0):
                line += '**'
            else:
                line += '  '
        print line

main()

