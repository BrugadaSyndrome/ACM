import sys

def farey(n):
    L = 1
    a, b, c, d = 0, 1, 1, n
    while (c <= n):
        k = int((n + b)/d)
        a, b, c, d = c, d, k*c - a, k*d - b
        #print "%d/%d" % (a,b)
        L += 1
    return L

def main():
    cases = int(sys.stdin.readline().strip())

    for c in range(cases):
        K, N = sys.stdin.readline().strip().split()
        K, N = int(K), int(N)

        print K, farey(N)

main()
