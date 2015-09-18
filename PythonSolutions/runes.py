# NOT DONE

import sys

def main():
    test_cases = int(sys.stdin.readline().strip())

    for t in range(test_cases):
        rune = sys.stdin.readline().strip()

        if (rune.find('+')):
            print rune.split('+')
        elif (rune.find('*')):
            print rune.split('*')
        elif (rune.find('-')):
            print rune.split('-')
        else:
            print "???", rune

        '''
        parts = []
        pos = 0
        prev = 0
        for L in rune:
            if (L in ['+', '-', '*', '=']):
                print rune[prev:pos]
                print rune[pos]
                prev = pos
            pos += 1
        print
        print
        '''
                


main()
