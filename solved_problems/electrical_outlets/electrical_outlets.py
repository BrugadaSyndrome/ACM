import sys


def main():
    num_test_cases = int(sys.stdin.readline().strip())
    for n in range(num_test_cases):
        line = sys.stdin.readline().strip().split()
        free_plugs = 0
        for i, plug_count in enumerate(line[1:]):
            if i == int(line[0])-1:
                # the last power strip will have all plugs available
                free_plugs += int(plug_count)
            else:
                # each power strip but the last one will have one plug used by the next power strip
                free_plugs += int(plug_count) - 1
        print(free_plugs)


main()
