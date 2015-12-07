import sys
import math

def distance(p1, p2):
    a = math.sqrt(pow(p1[0], 2) + pow(p1[1], 2))
    b = math.sqrt(pow(p2[0], 2) + pow(p2[1], 2))
    c = math.sqrt(pow(a, 2) + pow(b, 2))
    return c

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

    left5 = (left[0], left[1]-5)
    right5 = (right[0], right[1]+5)
    top5 = (top[0], top[1]+5)
    bottom5 = (bottom[0], bottom[1]-5)

    print 'left: {0}, -5: {1}'.format(left, left5)
    print 'right: {0}, +5 {1}'.format(right, right5)
    print 'top: {0}, +5: {1}'.format(top, top5)
    print 'bottom: {0}, -5: {1}'.format(bottom, bottom5)

    d_left_top = distance(left, right)
    d_top_right = distance(top, right)
    d_right_bottom = distance(right, bottom)
    d_bottom_left = distance(bottom, left)
    d_left_top5 = distance(left5, right5)
    d_top_right5 = distance(top5, right5)
    d_right_bottom5 = distance(right5, bottom5)
    d_bottom_left5 = distance(bottom5, left5)

    print 'left_top: {0}, 5: {1}'.format(d_left_top, d_left_top5)
    print 'top_right: {0}, 5: {1}'.format(d_top_right, d_top_right5)
    print 'right_bottom: {0}, 5: {1}'.format(d_right_bottom, d_right_bottom5)
    print 'bottom_left: {0}, 5: {1}'.format(d_bottom_left, d_bottom_left5)

    return 'no solution'

def main():
    cases = int(sys.stdin.readline().strip())

    for c in range(cases):
        positions = sys.stdin.readline().strip()
        x1, y1, x2, y2, x3, y3, x4, y4 = positions.split()

        print 'Case {0}: {1}'.format(c+1, fence_it([(int(x1), int(y1)), (int(x2), int(y2)), (int(x3), int(y3)), (int(x4), int(y4))]))

main()

#no solution
