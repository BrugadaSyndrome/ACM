import sys

def main():
    while(True):
        gallons = int(sys.stdin.readline().strip())

        if (gallons == 0):
            break

        print int(10000/gallons)
    

main()
