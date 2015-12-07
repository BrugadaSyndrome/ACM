import sys
import math

def get_prime_factors(number):
    if number <= 1:
        return []
    for i in xrange(2, number):
        rd, qt = divmod(number, i)
        if qt == 0:
            return [i] + get_prime_factors(rd)
    return [number]

# https://en.wikipedia.org/wiki/Euler%27s_totient_function
def ETF(n):
    factors = get_prime_factors(n)
    S = set()
    for f in factors:
        S.add(f)
    for f in S:
        p = (1 - (1.0/f))
        n *= p
    return n

def farey(n):
    if (n < 1):
        return 1
    return farey(n-1) + ETF(n)
    '''
    L = 1
    a, b, c, d = 0, 1, 1, n
    while (c <= n):
        k = int((n + b)/d)
        a, b, c, d = c, d, k*c - a, k*d - b
        #print "%d/%d" % (a,b)
        L += 1
    return L
    '''

def fareyList(n):
    F = [2]
    for i in range(2, n, 1):
        #F.append(int(farey(i)))
        F.append(int(F[i-2] + ETF(i)))
        #print i-1, F[i-2]
    return F

def main():
    sys.setrecursionlimit(10010)
    
    cases = int(sys.stdin.readline().strip())

    F = fareyList(10001)
    #print F

    for c in range(cases):
        K, N = sys.stdin.readline().strip().split()
        K, N = int(K), int(N)
        print K, F[N-1]
        #print K, int(farey(N)), (3*(N*N))/math.pi*math.pi

main()
