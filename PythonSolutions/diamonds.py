#NOT DONE

import sys

def highest(dia_dict):
    low_w = 11
    for w in sorted(dia_dict.keys()):
        if (w < low_w):
            low_w = w

    high_c = -1
    for c in sorted(dia_dict.keys()):
        if (c > high_c):
            high_c = c

    print low_w, dia_dict[low_w]
    print high_c, dia_dict[high_c]        

def main():
    test_cases = int(sys.stdin.readline().strip())

    for t in range(test_cases):
        diamonds = int(sys.stdin.readline().strip())

        dia_dict = {}
        for d in range(diamonds):
            w, c = sys.stdin.readline().strip().split()
            w = float(w)
            c = float(c)
            dia_dict[w] = c

        #highest(dia_dict)
        
        for d in sorted(dia_dict.keys()):
            print d, dia_dict[d]
        
        print
        print

main()
