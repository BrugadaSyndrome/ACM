# NOT DONE

import sys
import re

def decipher(n1, op, n2, s):
    for i in range(10):
        s1 = '{0}'.format(i).join(n1.split('?'))
        s2 = '{0}'.format(i).join(n2.split('?'))
        ss = '{0}'.format(i).join(s.split('?'))
        print s1+op+s2+'=='+ss
        if (eval(s1+op+s2+"=="+ss)):
            return i
    return -1

def main():
    test_cases = int(sys.stdin.readline().strip())

    for t in range(test_cases):
        rune = sys.stdin.readline().strip()
        match = re.match('(-?)([0-9?]+)([*+-])(-?)([0-9?]+)(=)(-?)([0-9?]+)', rune)    
        if (match):
            n1 = match.group(1) + match.group(2)
            op = match.group(3)
            n2 = match.group(4) + match.group(5)
            s = match.group(7) + match.group(8)
            
            print decipher(n1, op, n2, s)

main()
