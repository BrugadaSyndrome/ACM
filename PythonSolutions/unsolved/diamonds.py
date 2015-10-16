#NOT DONE

import sys        

def longest_sub(S, LS):
    for a in S:
        print '{0}>{1} and {2}<{3}'.format(a[0], LS[-1][0], a[1], LS[-1][1])
        if (a[0] > LS[-1][0] and a[1] < LS[-1][1]):
            LS.append(a)

    print LS 
    return LS

def main():
    test_cases = int(sys.stdin.readline().strip())

    for t in range(test_cases):
        diamonds = int(sys.stdin.readline().strip())

        # Sequence
        S = []
        for d in range(diamonds):
            w, c = sys.stdin.readline().strip().split()
            w, c = float(w), float(c)
            S.append((w, c))
            #print "({0}, {1})".format(w, c)


        print len(longest_sub(S, [S[0]]))

main()
