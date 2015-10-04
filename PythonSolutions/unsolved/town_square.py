import sys

def fence_it(positions):

    # find furthest points that must be fenced
    left = (101, 0)
    right = (-101, 0)
    top = (0, -101)
    bottom = (0, 101)
    for p in positions:
        if (p[0] < left[0]):
            left = p
        if (p[0] > right[0]):
            right = p
        if (p[1] > top[1]):
            top = p
        if (p[1] < bottom[1]):
            bottom = p

    # get side length
    s1 = abs(right[0] - left[0])
    s2 = abs(top[1] - bottom[1])

    #print left, right
    #print bottom, top
    #print s1, s2

    # invalid
    if (s1 == 0 or s2 == 0):
        return 'no solution'

    #valid, return longest side + 10 ft padding
    if (s1 > s2):
        return '{0:.2f}'.format(s1+10)
    else:
        return '{0:.2f}'.format(s2+10)

def main():
    cases = int(sys.stdin.readline().strip())

    for c in range(cases):
        positions = sys.stdin.readline().strip()
        x1, y1, x2, y2, x3, y3, x4, y4 = positions.split()

        print 'Case {0}: {1}'.format(c+1, fence_it([(int(x1), int(y1)), (int(x2), int(y2)), (int(x3), int(y3)), (int(x4), int(y4))]))

main()

#no solution
