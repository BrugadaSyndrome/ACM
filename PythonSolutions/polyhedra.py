import sys

def main():
    test_cases = int(sys.stdin.readline().strip())

    for t in range(test_cases):
        V, E = sys.stdin.readline().strip().split()
        V = int(V)
        E = int(E)
        F = 2 - V + E
        print F

main()
