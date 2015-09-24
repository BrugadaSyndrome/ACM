import sys

def purge(leaders, loser):
    pass

def minority(votes, leaders):
    return None

def majority(votes, leaders):
    for candidate in leaders.keys():
        if ( (leaders[candidate]/len(votes))*100 > 60 ):
            return (True, candidate)
    loser = minoriy(votes, leaders)
    purge(leaders, loser)
    return (False, loser)

def ranked_choice(votes):
    # Sum all the #1 votes
    leaders = {}
    for v in votes:
        v = v[0]
        if (v in leaders.keys()):
            ct = leaders[v]
            leaders[v] = ct+1
        else:
            leaders[v] = 1
    print leaders

    # Do we have a majority ?
    summary = ""
    while (True):
        result, candidate = majority(votes, leaders)
        if (result == True):
            summary += candidate
            return summary
        else:
            summary += '{0} -> '.format(candidate)
            return summary
    
    

    

def main():
    cases = int(sys.stdin.readline().strip())

    for c in range(cases):
        polls = int(sys.stdin.readline().strip())

        votes = []
        for p in range(polls):
            votes.append(sys.stdin.readline().strip())

        print ranked_choice(votes)


main()
