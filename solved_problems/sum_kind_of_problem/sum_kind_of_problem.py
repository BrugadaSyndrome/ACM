import sys

def main():
    cases = int(sys.stdin.readline().strip())

    for c in range(cases):
        S1 = 0
        S2 = 0
        S3 = 0
        K, N = sys.stdin.readline().strip().split()
        K, N = int(K), int(N)

        # firt N positive integers
        for i in range(N):
            S1 += i+1

        # first N odd integers
        for i in range(1, N*2, 2):
            S2 += i

        # first N even integers
        for i in range(0, N*2+1, 2):
            S3 += i

        print c+1, S1, S2, S3

main()
