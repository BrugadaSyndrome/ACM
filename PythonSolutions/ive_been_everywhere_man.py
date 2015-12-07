#ICPC 2015 - PROBLEM J

import sys

def main():
    tests = int(sys.stdin.readline().strip())

    for t in range(tests):
        num_cities = int(sys.stdin.readline().strip())

        cities = set()
        for c in range(num_cities):
            city = sys.stdin.readline().strip()
            cities.add(city)

        print len(cities)
            
main()
