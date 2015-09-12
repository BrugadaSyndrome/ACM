import sys

def translate(words):
    wd = '*'
    for w in range(len(words)-1):
        if (int(words[w]) == int(words[w+1])):
            wd += 'R'
        elif(int(words[w]) < int(words[w+1])):
            wd += 'U'
        else:
            wd += 'D'
    return wd

def main():
    melodies = int(sys.stdin.readline().strip())

    for mel in range(melodies):
        words = sys.stdin.readline().strip().split()[1:]
        print translate(words)

main()
