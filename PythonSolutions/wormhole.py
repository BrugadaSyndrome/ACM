# NOT DONE:
#   YES: ?closest planet via WH to p2, then cal the distance...?
#       - Case 1: Proxima to Earth is approx 7 but
#                 Proxima to Barnards = 0  and  Barnards to Earth is 5

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

def distance(p1, p2, planets, wormholes):
    # is there a free jump
    wh = wormholes.copy()
    if (free_jump(p1, p2, [], wh)):
        return 0

    # calc the distance
    p1x, p1y, p1z = planets[p1]
    p2x, p2y, p2z = planets[p2]
    return sqrt(pow(p2x-p1x, 2) + pow(p2y-p1y, 2) + pow(p2z-p1z, 2))

#'walk' the wormholes
def free_jump(start, goal, visited, wormholes):
    if (start == goal):
        #print 'Found it!'
        return True

    #ln 1 will most likely get key errors
    #print visited, "=>", start, "?", wormholes[start], '? =>', goal, '---', wormholes
    #print visited, "=>", start, "?=>", goal, '---', wormholes

    if (start in wormholes.keys()):
        for P in wormholes[start]:
            # make sure to not loop to previously visited planets
            if (P not in visited):
                #print start, '=>',
                return free_jump(P, goal, visited+[start], wormholes)
            else:
                #print "BEEN TO NEXT BEFORE BEFORE! next:", P,
                L = wormholes[start]
                #print 'CUR:', start ,'WHL:', L[1:]
                wormholes[start] = L[1:]
                return free_jump(start, goal, visited, wormholes)
    else:
        #print 'Dead End'
        return False

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
            if (from_p in wormholes.keys()):
                L = wormholes[from_p]
                wormholes[from_p] = L + [to_p]
            else:
                wormholes[from_p] = [to_p]

        #print wormholes

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
