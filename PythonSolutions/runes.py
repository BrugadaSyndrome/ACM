# NOT DONE

import sys
import re

def decipher(lhs, rhs):
    # parse rhs
    s_rhs = re.split('\\?', rhs)
    
    found_op = False
    s_lhs = ['!']
    
    #plus
    if (not found_op):
        plus = lhs.find('+')
        if (plus != -1):
            t = re.split('\\+', lhs)
            s_lhs = [t[0],'+',t[1]]
            found_op = 'plus'
            print 'plus: ', s_lhs, s_rhs
            
    #mult
    if (not found_op):
        mult = lhs.find('*')
        if (mult != -1):
            t = re.split('\\*', lhs)
            s_lhs = [t[0],'*',t[1]]
            found_op = 'mult'
            print 'mult: ', s_lhs, s_rhs

    #minus
    if (not found_op):
        sub = lhs.find('-')
        if (sub != -1):
            t = re.split('\\-', lhs)
            #n1-n2=sum
            if (len(t) == 2):
                s_lhs = [t[0],'-',t[1]]
                found_op = 'minus1'
            #n1--n2=sum
            elif (len(t) == 3 and t[0] != ''):
                 s_lhs = [t[0],'-',str(-1*int(t[-1]))]
                 found_op = 'minus2'
            #-n1-n2=sum
            elif (len(t) == 3 and t[0] == ''):
                s_lhs = [str(-1*int(t[1])),'-',t[2]]
                found_op = 'minus3'
            #-n1--n2=sum
            else:
                s_lhs = [str(-1*int(t[1])),'-',str(-1*int(t[-1]))]
                found_op = 'minus4'
            #print 'minus: ', s_lhs

    for i in range(10):
        var_lhs = re.split('\\?', ''.join(s_lhs))
        l = '{0}'.format(i).join(var_lhs)
        r = '{0}'.format(i).join(s_rhs)
        #print l, '=', r

        if (found_op == 'plus'):
            s1, s2 = l.split('+')
            n1, n2, nr = int(s1), int(s2), int(r)
            #print n1+n2, '==', r
            if ( (n1+n2) == nr):
                return i
        elif (found_op == 'mult'):
            s1, s2 = l.split('*')
            n1, n2, nr = int(s1), int(s2), int(r)
            #print n1*n2, '==', r
            if ((n1*n2) == nr):
                return i
        #n1-n2=sum
        elif (found_op == 'minus1'):
            s1, s2 = l.split('-')
            n1, n2, nr = int(s1), int(s2), int(r)
            #print 'm1 ', n1-n2, '==', r
            if ((n1-n2) == nr):
                return i
        #n1--n2=sum
        elif (found_op == 'minus2'):
            s = l.split('-')
            n1, n2, nr = int(s[0]), -1*int(s[2]), int(r)
            #print 'm2 ', n1-n2, '==', r
            if ((n1-n2) == nr):
                return i
        #-n1-n2=sum
        elif (found_op == 'minus3'):
            s = l.split('-')
            n1, n2, nr = -1*int(s[1]), int(s[2]), int(r)
            #print 'm3 ', n1-n2, '==', r
            if ((n1-n2) == nr):
                return i
        #-n1--n2=sum
        elif (found_op == 'minus4'):
            s = l.split('-')
            n1, n2, nr = -1*int(s[1]), -1*int(s[3]), int(r)
            #print 'm4 ', n1-n2, '==', r
            if ((n1-n2) == nr):
                return i
            
        
    return -1

def main():
    test_cases = int(sys.stdin.readline().strip())

    for t in range(test_cases):
        rune = sys.stdin.readline().strip()
        lhs, rhs = re.split('=', rune)
        print decipher(lhs, rhs)
        #print

def main2():
    test_cases = int(sys.stdin.readline().strip())

    for t in range(test_cases):
        rune = sys.stdin.readline().strip()
        match = re.match('(-?)([0-9?]+)([*+-])(-?)([0-9?]+)(=)(-?)([0-9?]+)', rune)
        if (match):
            for i in range(1, 9):
                print match.group(i)
            #print decipher2(n1, op, n2, s)

main2()
