import sys

def main():
    tests = int(sys.stdin.readline().strip())

    for t in range(tests):
        R, B, M = sys.stdin.readline().strip().split()
        R, B, M = float(R), float(B), float(M)

        '''
        add .5 and cast to int
        '''

        R /= 100.0
        for i in range(1200):
            #print i, B, M, math.ceil(100*B*R)/100.0
            I = int(((B * R)*100)+0.5)/100.0
            B = B + I - M
            #print i+1, B, R, I, M
            #B = math.ceil(100*((B + I) - M))/100.0
            #B = int((B + I) - M +.5)
            if (B <= 0):
                print i+1
                break
            if (i == 1199):
                print 'impossible'
                
            '''
            #print B
            #print B + (B * R/100.0)
            print i, int(1000 * (B + (B * R/100.0) - M))/1000.0
            B = int(1000 *(B + (B * R/100.0) - M))/1000.0
            if B <= 0:
                print i+1
                break
            if i == 1199:
                print 'impossible'
            '''

main()
