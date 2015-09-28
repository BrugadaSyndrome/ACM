import sys
import re
from decimal import Decimal
from fractions import Fraction

def find_fraction(dec):
    num = 1
    den = 1
    best_num = 129
    best_den = 129
    best_diff = 11
    for i in range(7):
        den *= 2
        for j in range(den-1):
            compare = '{0}./{1}'.format(num+j, den)
            ev = eval(compare) - dec
            print compare, eval(compare), dec, ev
            # difference is small enough and positive
            if (ev >= 0 and ev < .009):
            #if (ev >= 0):
            #if (abs(ev) < .009):
            
                if (best_diff > ev):
                    print '***', compare, eval(compare), dec, eval(compare) - dec
                    best_num = num+j
                    best_den = den
                    best_diff = ev
        
    return '{0}/{1}'.format(best_num, best_den)
        

def main():
    cases = int(sys.stdin.readline().strip())

    for c in range(cases):
        decimal = sys.stdin.readline().strip()
        match = re.match('([0-9]*)(\\.*)([0-9]*)', decimal)

        # valid input string
        if (match):
            # real number
            if (match.group(3) == '' or int(match.group(3)) == 0 ):
                print '{0}"'.format(int(match.group(1)))
                print
            # decimal number
            elif (match.group(1) == '' or int(match.group(1)) == 0):
                #print '? {0}"'.format(match.group(3))
                print '{0}"'.format(find_fraction(float('.{0}'.format(match.group(3)))))
                print
            # improper number
            else:
                #print '? {0} {1}"'.format(match.group(1), match.group(3))
                print '? {0} {1}"'.format(match.group(1), find_fraction(float('.{0}'.format(match.group(3)))))
                print
        else:
            print 'Input does not match: {0}'.format(decimal)
            

main()
