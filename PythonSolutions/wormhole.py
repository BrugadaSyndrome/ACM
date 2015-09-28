# NOT DONE

import sys
from math import sqrt

def parse_planet(planet_string):
    name, x, y, z = planet_string.split()
    x = int(x)
    y = int(y)
    z = int(z)
    return name, (x, y, z)

def distance(p1, p2, planets):
    p1x, p1y, p1z = planets[p1]
    p2x, p2y, p2z = planets[p2]
    return sqrt(pow(p2x-p1x, 2) + pow(p2y-p1y, 2) + pow(p2z-p1z, 2))

def closest_distance(S, G, PL, WH):
    wh = WH.copy()
    return walk_wormholes(S, G, [], PL, wh)

#'walk' the wormholes
def walk_wormholes(S, G, V, PL, WH):
    print V, "=>", S, '?=', G
    
    # arrived
    if (S == G):
        print 'Done'
        return 0

    # current distance
    CD = distance(S, G, PL)

    # keep looking along each wormhole path; return shortest distance
    if ( (S not in V) and (S in WH.keys()) ):
        for P in WH[S]:
            ND = walk_wormholes(P, G, V+[S], PL, WH)
            if (ND < CD):
                return ND
    # only step back if you have been somewhere
    elif( (len(V) > 1) ): #and (len(WH[V[-1]]) > 0) ):
            # remove dead end or loop branch
            WH[V[-1]] = WH[V[-1]][1:]
            # take a step back and keep looking
            PD = walk_wormholes(V[-1], G, V[:-1], PL, WH)
            if (PD < CD):
                return PD

    # no wormholes and have not found a better distance
    return CD

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
            from_p, to_p = sys.stdin.readline().strip().split()
            if (from_p in wormholes.keys()):
                L = wormholes[from_p]
                wormholes[from_p] = L + [to_p]
            else:
                wormholes[from_p] = [to_p]

        #queries
        num_queries = int(sys.stdin.readline().strip())
        queries = []
        for query in range(num_queries):
            queries.append(sys.stdin.readline().strip().split())

        print "Case {0}:".format(case+1)
        for q in queries:
            dist = closest_distance(q[0], q[1], planets, wormholes)
            print "The distance from {0} to {1} is {2} parsecs.".format(q[0], q[1], int(dist))

main()
