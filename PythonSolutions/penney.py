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

'''
prec = 100
==========
HHH HHH TIE 0 0 False
HHH HHT HHT 21 79 True
HHH HTH HHH 79 21 True
HHH THH THH 0 100 True
HHH HTT HTT 13 87 True
HHH THT HHH 71 29 True
HHH TTH TTH 6 94 True
HHH TTT HHH 61 39 True
HHT HHH HHT 68 32 True
HHT HHT TIE 0 0 False
HHT HTH HHT 100 0 True
HHT THH THH 0 100 True
HHT HTT HHT 95 5 True
HHT THT HHT 97 3 True
HHT TTH TTH 49 51 True
HHT TTT HHT 94 6 True
HTH HHH HHH 23 77 True
HTH HHT HHT 0 100 True
HTH HTH TIE 0 0 False
HTH THH THH 9 91 True
HTH HTT HTT 7 93 True
HTH THT HTH 61 39 True
HTH TTH TTH 6 94 True
HTH TTT TTT 30 70 True
THH HHH THH 100 0 True
THH HHT THH 100 0 True
THH HTH THH 92 8 True
THH THH TIE 0 0 False
THH HTT HTT 29 71 True
THH THT THH 83 17 True
THH TTH TTH 3 97 True
THH TTT THH 79 21 True
HTT HHH HTT 77 23 True
HTT HHT HHT 5 95 True
HTT HTH HTT 89 11 True
HTT THH THH 27 73 True
HTT HTT TIE 0 0 False
HTT THT HTT 91 9 True
HTT TTH HTT 100 0 True
HTT TTT HTT 99 1 True
THT HHH HHH 28 72 True
THT HHT HHT 6 94 True
THT HTH HTH 49 51 True
THT THH THH 7 93 True
THT HTT HTT 4 96 True
THT THT TIE 0 0 False
THT TTH TTH 0 100 True
THT TTT TTT 23 77 True
TTH HHH TTH 92 8 True
TTH HHT HHT 6 94 True
TTH HTH TTH 93 7 True
TTH THH TTH 92 8 True
TTH HTT HTT 0 100 True
TTH THT TTH 99 1 True
TTH TTH TIE 0 0 False
TTH TTT TTH 71 29 True
TTT HHH TTT 52 48 True
TTT HHT HHT 3 97 True
TTT HTH TTT 68 32 True
TTT THH THH 16 84 True
TTT HTT HTT 0 100 True
TTT THT TTT 84 16 True
TTT TTH TTH 20 80 True
TTT TTT TIE 0 0 False
HHT
TTH
HHH
TIE

prec = 10000
============
HHH HHH TIE 0 0 False
HHH HHT HHT 2644 7356 True
HHH HTH HHH 7708 2292 True
HHH THH THH 2 9998 True
HHH HTT HTT 1300 8700 True
HHH THT HHH 7251 2749 True
HHH TTH TTH 355 9645 True
HHH TTT HHH 5333 4667 True
HHT HHH HHT 7096 2904 True
HHT HHT TIE 0 0 False
HHT HTH HHT 9994 6 True
HHT THH THH 15 9985 True
HHT HTT HHT 9513 487 True
HHT THT HHT 9503 497 True
HHT TTH TTH 2103 7897 True
HHT TTT HHT 9346 654 True
HTH HHH HHH 3051 6949 True
HTH HHT HHT 4 9996 True
HTH HTH TIE 0 0 False
HTH THH THH 369 9631 True
HTH HTT HTT 765 9235 True
HTH THT HTH 5261 4739 True
HTH TTH TTH 532 9468 True
HTH TTT TTT 3010 6990 True
THH HHH THH 10000 0 True
THH HHT THH 9975 25 True
THH HTH THH 9646 354 True
THH THH TIE 0 0 False
THH HTT HTT 2671 7329 True
THH THT THH 8721 1279 True
THH TTH TTH 385 9615 True
THH TTT THH 8017 1983 True
HTT HHH HTT 7952 2048 True
HTT HHT HHT 559 9441 True
HTT HTH HTT 8810 1190 True
HTT THH THH 2353 7647 True
HTT HTT TIE 0 0 False
HTT THT HTT 9717 283 True
HTT TTH HTT 9998 2 True
HTT TTT HTT 10000 0 True
THT HHH HHH 3182 6818 True
THT HHT HHT 366 9634 True
THT HTH THT 5188 4812 True
THT THH THH 820 9180 True
THT HTT HTT 295 9705 True
THT THT TIE 0 0 False
THT TTH TTH 6 9994 True
THT TTT TTT 2913 7087 True
TTH HHH TTH 9343 657 True
TTH HHT HHT 2016 7984 True
TTH HTH TTH 9332 668 True
TTH THH TTH 9472 528 True
TTH HTT HTT 19 9981 True
TTH THT TTH 9990 10 True
TTH TTH TIE 0 0 False
TTH TTT TTH 6911 3089 True
TTT HHH TTT 5646 4354 True
TTT HHT HHT 293 9707 True
TTT HTH TTT 7405 2595 True
TTT THH THH 1304 8696 True
TTT HTT HTT 3 9997 True
TTT THT TTT 7791 2209 True
TTT TTH TTH 2402 7598 True
TTT TTT TIE 0 0 False
HHT
TTH
HHH
TIE

prec =  100000
==============
HHH HHH TIE 0 0
HHH HHT HHT 2594 7406
HHH HTH HHH 7852 2148
HHH THH THH 4 9996
HHH HTT HTT 1286 8714
HHH THT HHH 7287 2713
HHH TTH TTH 403 9597
HHH TTT HHH 5287 4713
HHT HHH HHT 7007 2993
HHT HHT TIE 0 0
HHT HTH HHT 9994 6
HHT THH THH 10 9990
HHT HTT HHT 9477 523
HHT THT HHT 9534 466
HHT TTH TTH 3049 6951
HHT TTT HHT 9501 499
HTH HHH HHH 2803 7197
HTH HHT HHT 6 9994
HTH HTH TIE 0 0
HTH THH THH 351 9649
HTH HTT HTT 785 9215
HTH THT HTH 5273 4727
HTH TTH TTH 490 9510
HTH TTT TTT 3019 6981
THH HHH THH 10000 0
THH HHT THH 9988 12
THH HTH THH 9614 386
THH THH TIE 0 0
THH HTT HTT 2889 7111
THH THT THH 8883 1117
THH TTH TTH 465 9535
THH TTT THH 7914 2086
HTT HHH HTT 8020 1980
HTT HHT HHT 398 9602
HTT HTH HTT 8757 1243
HTT THH THH 2398 7602
HTT HTT TIE 0 0
HTT THT HTT 9746 254
HTT TTH HTT 9978 22
HTT TTT HTT 9999 1
THT HHH HHH 3176 6824
THT HHT HHT 323 9677
THT HTH THT 5405 4595
THT THH THH 857 9143
THT HTT HTT 324 9676
THT THT TIE 0 0
THT TTH TTH 6 9994
THT TTT TTT 2793 7207
TTH HHH TTH 9446 554
TTH HHT HHT 2437 7563
TTH HTH TTH 9398 602
TTH THH TTH 9434 566
TTH HTT HTT 19 9981
TTH THT TTH 9995 5
TTH TTH TIE 0 0
TTH TTT TTH 7093 2907
TTT HHH TTT 5568 4432
TTT HHT HHT 282 9718
TTT HTH TTT 7586 2414
TTT THH THH 1545 8455
TTT HTT HTT 3 9997
TTT THT TTT 7832 2168
TTT TTH TTH 1872 8128
TTT TTT TIE 0 0
HHT
TTH
HHH
TIE

prec = 10000000
===============
HHH HHH TIE 0 0
HHH HHT HHT 267177 732823
HHH HTH HHH 762642 237358
HHH THH THH 115 999885
HHH HTT HTT 122002 877998
HHH THT HHH 721958 278042
HHH TTH TTH 29844 970156
HHH TTT HHH 525693 474307
HHT HHH HHT 690864 309136
HHT HHT TIE 0 0
HHT HTH HHT 999625 375
HHT THH THH 971 999029
HHT HTT HHT 949399 50601
HHT THT HHT 952248 47752
HHT TTH TTH 203264 796736
HHT TTT HHT 943012 56988
HTH HHH HHH 297177 702823
HTH HHT HHT 334 999666
HTH HTH TIE 0 0
HTH THH THH 39270 960730
HTH HTT HTT 72848 927152
HTH THT HTH 533026 466974
HTH TTH TTH 38842 961158
HTH TTT TTT 308030 691970
THH HHH THH 999886 114
THH HHT THH 999267 733
THH HTH THH 956629 43371
THH THH TIE 0 0
THH HTT HTT 256804 743196
THH THT THH 878456 121544
THH TTH TTH 42599 957401
THH TTT THH 789707 210293
HTT HHH HTT 790345 209655
HTT HHT HHT 39904 960096
HTT HTH HTT 872932 127068
HTT THH THH 217219 782781
HTT HTT TIE 0 0
HTT THT HTT 970907 29093
HTT TTH HTT 998539 1461
HTT TTT HTT 999829 171
THT HHH HHH 324346 675654
THT HHT HHT 34263 965737
THT HTH THT 530571 469429
THT THH THH 75488 924512
THT HTT HTT 32013 967987
THT THT TIE 0 0
THT TTH TTH 409 999591
THT TTT TTT 286180 713820
TTH HHH TTH 923459 76541
TTH HHT HHT 212591 787409
TTH HTH TTH 922745 77255
TTH THH TTH 929612 70388
TTH HTT HTT 999 999001
TTH THT TTH 999600 400
TTH TTH TIE 0 0
TTH TTT TTH 659488 340512
TTT HHH TTT 543949 456051
TTT HHT HHT 29380 970620
TTT HTH TTT 741521 258479
TTT THH THH 133100 866900
TTT HTT HTT 190 999810
TTT THT TTT 766875 233125
TTT TTH TTH 261242 738758
TTT TTT TIE 0 0
HHT
TTH
HHH
TIE
'''
