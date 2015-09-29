import sys

def majority(votes):
    for v in votes.keys():
        if ((votes[v]*1./len(votes))*100 > 60):
            return votes[v]
    return None

def winner(F, S, T):
    W = majority(F)

def ranked_choice(votes):
    first = {}
    second = {}
    third = {}
    for v in votes:
        for p in range(len(v)):
            # first place vote
            if (p == 0):
                if (v[p] not in first.keys()):
                    first[v[p]] = 1
                else:
                    first[v[p]] = first[v[p]] + 1
            # second place vote
            elif (p == 1):
                if (v[p] not in second.keys()):
                    second[v[p]] = 1
                else:
                    second[v[p]] = second[v[p]] + 1
            # third place vote
            elif (p == 2):
                if (v[p] not in third.keys()):
                    third[v[p]] = 1
                else:
                    third[v[p]] = third[v[p]] + 1

    W = winner(first, second, third)
    return W

def main():
    cases = int(sys.stdin.readline().strip())

    for c in range(cases):
        polls = int(sys.stdin.readline().strip())

        votes = []
        for p in range(polls):
            votes.append(sys.stdin.readline().strip())

        print ranked_choice(votes)
        print


main()
