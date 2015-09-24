import sys
from math import sqrt

def parse_planet(planet_string):
    name, x, y, z = planet_string.split()
    x = int(x)
    y = int(y)
    z = int(z)
    return name, (x, y, z)

def parse_wormhole(wormhole_string):
    return wormhole_string.split()

def parse_query(query_string):
    return query_string.split()

#recursively search wormholes for a valid free jump path
def free_jump(p1, p2, wormholes):
    #print p1, "=>",
    if (p1 not in wormholes.keys()):
        #print 'No path'
        return False
    
    if (wormholes[p1] == p2):
        #print p2, 'Done'
        return True
    else:
        return free_jump(wormholes[p1], p2, wormholes)

def distance(p1, p2, planets, wormholes):
    # is there a free jump
    if (free_jump(p1, p2, wormholes)):
        return 0

    # calc the distance
    p1x, p1y, p1z = planets[p1]
    p2x, p2y, p2z = planets[p2]
    return sqrt(pow(p2x-p1x, 2) + pow(p2y-p1y, 2) + pow(p2z-p1z, 2))

def main():
    num_cases = int(sys.stdin.readline().strip())
    
    for case in range(num_cases):
        #planets
        num_planets = int(sys.stdin.readline().strip())
        planets = {}
        for planet in range(num_planets):
            name, loc = parse_planet(sys.stdin.readline().strip())
            planets[name] = loc
            
        #wormholes
        num_wormholes = int(sys.stdin.readline().strip())
        wormholes = {}
        for wormhole in range(num_wormholes):
            from_p, to_p = parse_wormhole(sys.stdin.readline().strip())
            wormholes[from_p] = to_p

        #queries
        num_queries = int(sys.stdin.readline().strip())
        queries = []
        for query in range(num_queries):
            queries.append(parse_query(sys.stdin.readline().strip()))

        print "Case {0}:".format(case+1)
        for q in queries:
            dist = distance(q[0], q[1], planets, wormholes)
            print "The distance from {0} to {1} is {2} parsecs.".format(q[0], q[1], int(dist))

main()
