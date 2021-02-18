import sys

def make_key(vote):
    v1, v2, v3 = '', '', ''
    if (len(vote) == 3):
        v3 = vote[2]
    if (len(vote) >= 2):
        v2 = vote[1]
    if (len(vote) >= 1):
        v1 = vote[0]
    return (v1,v2,v3)

def main():
    cases = int(sys.stdin.readline().strip())

    for c in range(cases):
        polls = int(sys.stdin.readline().strip())

        votes = {}
        for p in range(polls):
            vote = sys.stdin.readline().strip()
            k = make_key(vote)
            if (k in votes.keys()):
                votes[k] = votes[k]+1
            else:
                votes[k] = 1
        print votes
                         
main()
