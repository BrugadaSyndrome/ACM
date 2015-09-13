import sys

'''
def T(n):
    total = 0
    for i in range(n):
        total += 1 * (i+1) - 0
    print 'T', n, total
    return total

def S(n):
    total = 0
    for i in range(n):
        total += 2 * (i+1) - 1
    print 'S', n, total
    return total

def P(n):
    total = 0
    for i in range(n):
        total += 3 * (i+1) - 2
    print 'P', n, total
    return total

def H(n):
    total = 0
    for i in range(n):
        total += 4 * (i+1) - 3
    print 'H', n, total
    return total

def total_pairs(pairs):
    total = 0
    for i in range(0, len(pairs), 2):
        if(int(pairs[i]) == 3):
            total += T(int(pairs[i+1]))
        elif(int(pairs[i]) == 4):
            total += S(int(pairs[i+1]))
        elif(int(pairs[i]) == 5):
            total += P(int(pairs[i+1]))
        elif(int(pairs[i]) == 6):
            total += H(int(pairs[i+1]))
    print total
    return total % 255
'''

def figurate(pairs):
    total = 0
    for i in range(0, len(pairs), 2):
        poly = pairs[i]
        num_dots = pairs[i+1]
        mult = int(poly)-2
        diff = int(poly)-3
        for j in range(int(num_dots)):
            total += mult * (j+1) - diff
    return total

def main():
    lines = int(sys.stdin.readline().strip())

    results = []
    for l in range(lines):
        pairs = sys.stdin.readline().strip().split()[1:]
        #results.append(chr(total_pairs(pairs)))
        results.append(chr(figurate(pairs)))

    print ''.join(results)

main()

