#DOES WORK: BUT does not meet the time limit
            #remove blank ballots
            #? lump duplicate ballots together and add a multiplier to the ballot class

import sys
import random
import time

rank_time = 0
majority_time = 0

class Ballot():
    def __init__(self, A, B, C):
        self.votes = [A, B, C]

    def first(self):
        return self.votes[0]

    def second(self):
        return self.votes[1]

    def third(self):
        return self.votes[2]
    
    def purge(self, Z):
        new_votes = []
        for C in self.votes:
            if (C not in Z):
                new_votes.append(C)
        while (len(new_votes) != len(self.votes)):
            new_votes.append(None)
        self.votes = new_votes

    def __eq__(self, rhs):
        if (self.first() == rhs.first()):
            if (self.second() == rhs.second()):
                if (self.third() == rhs.third()):
                    return True
        return False
    def __str__(self):
        return 'B: {0} {1} {2}'.format(self.first(), self.second(), self.third())

def rank(votes):
    ###
    global rank_time
    T = time.time()
    ###
    first = {}
    fc = 0
    second = {}
    sc = 0
    third = {}
    tc = 0
    for v in votes:
        if (v.first() != None):
            fc += 1
            if (v.first() not in first.keys()):
                first[v.first()] = 1
            else:
                first[v.first()] = first[v.first()] + 1

        if (v.second() != None):
            sc += 1
            if (v.second() not in second.keys()):
                second[v.second()] = 1
            else:
                second[v.second()] = second[v.second()] + 1

        if (v.third() != None):
            tc += 1
            if (v.third() not in third.keys()):
                third[v.third()] = 1
            else:
                third[v.third()] = third[v.third()] + 1

    ###
    rank_time += time.time() - T
    ###
    return [first, fc], [second, sc], [third, tc]

def majority(votes, first, fc, second, sc, third, tc):
    ###
    global majority_time
    T = time.time()
    ###
    #print first, second, third
    # eliminated all candidates
    if (len(first.keys()) == 0):
        return 'no winner'
    # found a majority winner
    for candidate in first.keys():
        #print candidate, (first[candidate]*1.0/fc)*100
        if ((first[candidate]*1.0/fc)*100 > 50):
            return candidate
    # eliminate candidates with no first palce votes
    loser_dict = {}
    for v in votes:
        #if (v.first() != None and v.first() not in first.keys() and v.first() not in losers):
        #    losers.append(v.first())
        if (v.second() != None and v.second() not in first.keys()):
            loser_dict[v.second()] = None
        if (v.third() != None and v.third() not in first.keys()):
            loser_dict[v.third()] = None
    losers = loser_dict.keys()
    #print 'losers: ', losers

    # eliminate candidates with the least amount of first place votes
    if (len(losers) == 0):
        minority = []
        low = 10001
        for v in first.keys():
            if (first[v] < low):
                minority = [v]
                low = first[v]
            elif (first[v] == low):
                minority.append(v)
        losers = minority

    # purge losers
    for v in votes:
        if (v.first() != None):
            v.purge(losers)
    # remove blank ballots
    
    

    ###
    majority_time += time.time() - T
    ###
    nfirst, nsecond, nthird = rank(votes)
    return '{0} -> '.format(''.join(sorted(losers))) + majority(votes, nfirst[0], nfirst[1], nsecond[0], nsecond[1], nthird[0], nthird[1])

def ranked_choice(votes):
    first, second, third = rank(votes)
    return majority(votes, first[0], first[1], second[0], second[1], third[0], third[1])

def generate_test(cases, num_votes):
    candidates = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    fout = open('votes.txt', 'w')
    fout.write('{0}\n'.format(cases))
    for i in range(cases):
        fout.write('{0}\n'.format(num_votes))
        for i in range(num_votes):
            fout.write(random.choice(candidates)+random.choice(candidates)+random.choice(candidates)+'\n')
    fout.close()

def main():
    ###
    random.seed(time.clock())
    cases = 100
    num_votes = 1000
    generate_test(cases, num_votes)
    ###
    
    cases = int(sys.stdin.readline().strip())

    ###
    start_time = time.time()
    ###
    for c in range(cases):
        polls = int(sys.stdin.readline().strip())

        votes = {}
        for p in range(polls):
            vote = sys.stdin.readline().strip()
            v1, v2, v3 = '', '', ''
            if (len(vote) == 3):
                v3 = vote[2]
            if (len(vote) >= 2):
                v2 = vote[1]
            if (len(vote) >= 1):
                v1 = vote[0]
            k = v1+v2+v3
                
            if (k in votes.keys()):
                votes[k] = votes[k]+1
            else:
                votes[k] = 1
            #votes.append(Ballot(v1, v2, v3))
        print votes

        ###
        case_time = time.time()
        global rank_time
        global majority_time
        rank_time = 0
        majority_time = 0
        ###
        #print ranked_choice(votes)
        ###
        print("--- %s rank seconds ---" % (rank_time))
        print("--- %s majority seconds ---" % (majority_time))
        print("--- %s case seconds ---" % (time.time() - case_time))
        ###
        
    ###
    print("--- %s set seconds ---" % (time.time() - start_time))
    ###
                         
main()
