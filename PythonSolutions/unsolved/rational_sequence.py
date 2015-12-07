import sys

def seq(p, q, a, b):
    print 'a:', a, 'b:', b
    if (a > 100 or b > 100):
        return -1
    
    # found it
    if (p == a and q == b):
        return 1
    # right branch
    elif (a < p):
        return seq(p, q, a+b, b)
    # left branch
    elif (b < q):
        return seq(p, q, a, a+b)
    return -1

def main():
    cases = int(sys.stdin.readline().strip())

    for c in range(cases):
        K, R = sys.stdin.readline().strip().split()
        K = int(K)
        P, Q = R.split('/')

        print K, seq(int(P), int(Q), 1, 1)

main()
