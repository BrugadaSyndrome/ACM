import math
import random
import sys
import time

poss_patterns = ['HHH', 'HHT', 'HTH', 'THH', 'HTT', 'THT', 'TTH', 'TTT']
flip_dict = {}

def flip():
    #if (int((time.clock()*1000000)%2) == 0):
    if (random.randint(0, 1000000)%2 == 0):
        return 'H'
    else:
        return 'T'

def flip_series(a, b):
    series = ""
    while(True):
        series += flip()
        #print series, series[-3:], a, b
        if (series[-3:] == a):
            return a
        elif (series[-3:] == b):
            return b

def calc_probs():
    prec = 10000
    for a in poss_patterns:
        for b in poss_patterns:
            p1 = 0
            p2 = 0
            if (a == b): # or ((a=="HHH" or b=="TTT")or(a=="TTT" or b =="HHH"))):
                flip_dict[(a, b)] = "TIE"
            else:
                for i in range(prec):
                    r = flip_series(a, b)
                    if (r == a):
                        p1 += 1
                    elif(r == b):
                        p2 += 1
                        
                t = p1+p2
                if ( (p1 == p2) or (math.fabs(100*((float(p1)/t)-(float(p2)/t))) < 10) ):
                    flip_dict[(a, b)] = "TIE"
                elif (p1 > p2):
                    flip_dict[(a, b)] = a
                else:
                    flip_dict[(a, b)] = b

                '''
                if ((math.fabs(100*((float(p1)/t)-(float(p2)/t))) < 10)):
                    print a, b, flip_dict[(a, b)], '{0} < 10% diff'.format(math.fabs(100*((float(p1)/t)-(float(p2)/t))))
                else:
                    print a, b, flip_dict[(a, b)], '{0} > 10% diff'.format(math.fabs(100*((float(p1)/t)-(float(p2)/t))))
                #, float(p1)/t, float(p2)/t, ))<10 #, p1+p2==prec
                '''

def main():
    random.seed(time.clock())

    calc_probs()

    compares = int(sys.stdin.readline().strip())

    for c in range(compares):
        p1, p2 = sys.stdin.readline().strip().split()
        print flip_dict[(p1, p2)]

main()
