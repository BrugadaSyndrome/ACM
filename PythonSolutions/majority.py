import sys

def main():
    test_cases = int(sys.stdin.readline().strip())

    for t in range(test_cases):
        totals = {}
        votes = int(sys.stdin.readline().strip())

        for v in range(votes):
            vote = int(sys.stdin.readline().strip())
            if vote in totals.keys():
                cc = totals[vote]
                cc += 1
                totals[vote] = cc
            else:
                totals[vote] = 1

        cur_value = -1
        cur_key = -1
        for k in sorted(totals.keys()):
            if (totals[k] > cur_value):
                cur_key = k
                cur_value = totals[k]
            
        print cur_key

main()
