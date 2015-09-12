import sys

def main():
    while(True):
        start_rocks = int(sys.stdin.readline().strip())

        if (start_rocks == 0):
            break

        current_rocks = start_rocks
        piles = 0
        while (current_rocks != 1):
            # Even number of rocks in pile
            if (current_rocks % 2 == 0):
                current_rocks /= 2
            # Odd number of rocks in pile
            else:
                current_rocks = (current_rocks * 3) + 1
            piles += 1

        print start_rocks, piles
                

main()
