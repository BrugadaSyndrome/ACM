# NOT DONE: Most likely not walking all paths so is not garaunteed to find the shortest path

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
'''
def walk_wormholes(start, goal, visited, wormholes, planets):
    if (start == goal):
        #print 'Found it!'
        return 0

    #ln 1 will most likely get key errors
    #print visited, "=>", start, "?", wormholes[start], '? =>', goal, '---', wormholes
    #print visited, "=>", start, "?=>", goal, '---', wormholes
    #print visited, "=>", start, "?=>", goal, '~', distance(start, goal, planets)

    cur_dist = distance(start, goal, planets)

    if (start in wormholes.keys()):
        for P in wormholes[start]:
            # make sure to not loop to previously visited planets
            if (P not in visited):
                #print start, '=>',
                best_dist = walk_wormholes(P, goal, visited+[start], wormholes, planets)
                next_dist = distance(P, goal, planets)
                #print '{0} < {1} ? {2}'.format(cur_dist, best_dist, cur_dist<best_dist)
                if (cur_dist < next_dist):
                    return cur_dist
                else:
                    return next_dist
            else:
                #print "BEEN TO NEXT BEFORE BEFORE! next:", P,
                L = wormholes[start]
                wormholes[start] = L[1:]
                best_dist = walk_wormholes(start, goal, visited, wormholes, planets)
                return best_dist
    
    #print 'Dead End'
    return cur_dist
'''
def walk_wormholes(S, G, V, PL, WH):
    print V, "=>", S, '?=', G
    
    # arrived
    if (S == G):
        print 'Done'
        return 0

    if (S in WH.keys()):
        #check out each node connected by an edge
        for P in WH[S]:
            CD = distance(S, G, PL)
            # looped: remove S->P edge and backtrack
            if (P in V):
                WH[S] = WH[S][1:]
                BD = walk_wormholes(V[-1], G, V[:-1], PL, WH)
                print CD, "?<", BD
                if (CD < BD):
                    return CD
                else:
                    return BD
            # keep exploring
            else:
                print 'Keep Walking'
                BD = walk_wormholes(P, G, V+[S], PL, WH)
                print CD, "?<", BD
                if (CD < BD):
                    return CD
                else:
                    return BD
    else:
        return distance(S, G, PL)

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
