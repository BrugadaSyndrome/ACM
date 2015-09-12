import sys

def main():
    H, W = sys.stdin.readline().strip().split()

    for w in range(int(W)):
        row = ""
        for h in range(int(H)):
            row += '*'
        print row

main()
