import sys

def find_path(p, q):
    if (p == 1 and q == 1):
        #print '{0}/{1} -> Head'.format(p, q)
        return 'H'[::-1]
    elif (p < q):
        #print '{0}/{1} -> L'.format(p, q)
        return 'L' + find_path(p, abs(p-q))
    elif (p > q):
        #print '{0}/{1} -> R'.format(p, q)
        return 'R' + find_path(abs(p-q), q)
    return -1

def main():
    cases = int(sys.stdin.readline().strip())

    for c in range(cases):
        K, R = sys.stdin.readline().strip().split()
        K = int(K)
        P, Q = R.split('/')

        path = find_path(int(P), int(Q))[::-1]
        binary_path = ''
        for step in path:
            if (step == 'H'):
                binary_path += '1'
            if (step == 'L'):
                binary_path += '0'
            elif (step == 'R'):
                binary_path += '1'
        
        print K, int(binary_path, 2)

main()
