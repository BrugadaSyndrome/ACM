import sys

devlali = {}

def sum_number(number):
    str_n = str(number)
    total = 0
    for n in str_n:
        total += int(n)
    return total + number

def generate_devlali():
    for i in range(10001):
        total = sum_number(i)
        if (total in devlali.keys()):
            tmp_list = devlali[total]
            tmp_list.append(i)
            devlali[total] = tmp_list
        else:
            devlali[total] = [i]

def get_devlali(number):
    if (number in devlali.keys()):
        if (len(devlali[number]) > 1):
            return 'junction'
        else:
            return 'generated'
    else:
        return 'self'

def main():
    generate_devlali()
    
    lines = int(sys.stdin.readline().strip())

    for num in range(lines):
        n = int(sys.stdin.readline().strip())
        print n, get_devlali(n)

main()
