import sys
import re
import math

def equal(D1, D2, ACC):
    RU = math.ceil(D2*pow(10, ACC))
    RD = math.floor(D2*pow(10, ACC))
    #print D2, RU, RD
    if (D1 in [RU, RD]):
        return True
    return False

def dec_eq_fract(dec, fract):
    L = len(dec)
    int_dec = int(dec)
    for f in fract:
        if (equal(int_dec, f[1], L)):
            return f[0]
    return -1

def generate_fractions():
    fracts = []
    num = 1
    den = 1
    for i in range(7):
        den *= 2
        for j in range(den-1):
            fract = '{0}/{1}'.format(num+j, den)
            dec = eval('{0}./{1}'.format(num+j, den))
            fracts.append((fract, dec))
        
    return fracts
        

def main():
    cases = int(sys.stdin.readline().strip())
    fracts = generate_fractions()

    for c in range(cases):
        decimal = sys.stdin.readline().strip()
        match = re.match('([0-9]*)(\\.*)([0-9]*)', decimal)

        # valid input string
        if (match):
            # real number
            if (match.group(3) == '' or int(match.group(3)) == 0 ):
                print '{0}"'.format(int(match.group(1)))
            # decimal number
            elif (match.group(1) == '' or int(match.group(1)) == 0):
                #print '? {0}"'.format(match.group(3))
                print '{0}"'.format(dec_eq_fract(match.group(3), fracts))
            # improper number
            else:
                #print '? {0} {1}"'.format(match.group(1), match.group(3))
                print '{0} {1}"'.format(match.group(1), dec_eq_fract(match.group(3), fracts))
        else:
            print 'Input does not match: {0}'.format(decimal)
            

main()
