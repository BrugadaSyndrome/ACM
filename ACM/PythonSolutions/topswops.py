import sys

def topswops(deck):
    swaps = 0
    while(int(deck[0]) != 1):
        top = deck[:int(deck[0])]
        top.reverse()
        top += deck[int(deck[0]):]
        deck = top
        swaps += 1
    return swaps    

def main():
    deck_size = int(sys.stdin.readline().strip())
    num_decks = int(sys.stdin.readline().strip())

    for nd in range(num_decks):
        deck = sys.stdin.readline().strip().split()
        print topswops(deck)

main()
