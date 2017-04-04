import sys

def main():
    num_words = int(sys.stdin.readline().strip())

    words = []
    anagrams = {}
    for w in range(num_words):
        words.append(sys.stdin.readline().strip())
        sorted_word = ''.join(sorted(words[w]))
        if (sorted_word in anagrams.keys()):
            tmp_list = anagrams[sorted_word]
            tmp_list.append(words[w])
            anagrams[sorted_word] = sorted(tmp_list)
        else:
            anagrams[sorted_word] = [words[w]]

    for k in sorted(anagrams.keys()):
        print k,
        word_list = anagrams[k]
        for w in range(len(word_list)):
            if (w != len(word_list)-1):
                print word_list[w],
            else:
                print word_list[w]

main()
