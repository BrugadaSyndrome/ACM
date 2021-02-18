import sys

def main():
    num_lines = int(sys.stdin.readline().strip())

    for line in range(num_lines):
        word1, word2 = sys.stdin.readline().strip().split()
        if (word1 == word2):
            print "{0} and {1} are the same".format(word1, word2)
        else:
            print "{0} and {1} are different".format(word1, word2)

main()
