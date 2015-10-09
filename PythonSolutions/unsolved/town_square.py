import math
import sys

def slope(p1, p2):
    num = p2[1]-p1[1]
    den = p2[0]-p1[0]
    if (den == 0):
        return 'U'
    #print p1, p2, num, den
    return num/den

def point_distance(p1, p2):
    a = p2[1]-p1[1]
    b = p2[0]-p1[0]
    c = math.sqrt(pow(a, 2) + pow(b, 2))
    return c

def sin_distance(d, theta, phi):
    return (math.sin(theta) * math.sin(phi)) / d

def fence_it(positions):

    # determine the furthest points
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

    #print 'L:{0} R:{1} B:{2} T:{3}'.format(left, right, bottom, top)

    # adjust so that origin is equal to bottom
    adjust = bottom
    left = (left[0]-adjust[0], left[1]-adjust[1])
    right = (right[0]-adjust[0], right[1]-adjust[1])
    bottom = (bottom[0]-adjust[0], bottom[1]-adjust[1])
    top = (top[0]-adjust[0], top[1]-adjust[1])
    min_slope = slope(left, bottom)
    max_slope = slope(bottom, right)

    # min/max slopes
    if (min_slope == 'U'):
        min_slope = -200
    if (max_slope == 'U'):
        max_slope = 200

    print 'La:{0} Ra:{1} Ba:{2} Ta:{3}'.format(left, right, bottom, top)
    print 'min-slope:{0} right-slope:{1}'.format(min_slope, max_slope)

    slopes = []
    begin = min_slope
    end = max_slope
    step = 0.1
    while (begin <= end):
        slopes.append(int(begin*10)/10.0)
        begin = begin + step

    '''  
    for s in slopes:
        d1 = point_distance(bottom, left)
        d2 = sin_distance(d1, 90, s)
        print 'd1:{0} d2:{1} d3:{2}'.format(d1, d2, d3)
    '''
        
    print slopes
    
    return 'no solution'

def main():
    cases = int(sys.stdin.readline().strip())

    for c in range(cases):
        positions = sys.stdin.readline().strip()
        x1, y1, x2, y2, x3, y3, x4, y4 = positions.split()

        print 'Case {0}: {1}'.format(c+1, fence_it([(int(x1), int(y1)), (int(x2), int(y2)), (int(x3), int(y3)), (int(x4), int(y4))]))
        print
        
main()

#no solution
