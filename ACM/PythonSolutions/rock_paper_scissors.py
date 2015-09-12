import sys

def winner(A, B):
    if (A == 'Rock'):
        if (B == 'Paper'):
            return 'B'
        if (B == 'Scissors'):
            return 'A'
    if (A == 'Paper'):
        if (B == 'Rock'):
            return 'A'
        if (B == 'Scissors'):
            return 'B'
    if (A == 'Scissors'):
        if (B == 'Rock'):
            return 'B'
        if (B == 'Paper'):
            return 'A'

def main():
    num_lines = int(sys.stdin.readline().strip())

    for line in range(num_lines):
        A, B = sys.stdin.readline().strip().split()
        if (A == B):
            print 'tie'
        elif (winner(A, B) == 'A'):
            print 'A wins'
        else:
            print 'B wins'

main()
