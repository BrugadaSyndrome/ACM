import sys

def main():
    num_digits = int(sys.stdin.readline().strip())
    nums_to_generate = int(sys.stdin.readline().strip())
    seed = int(sys.stdin.readline().strip())

    for num in range(nums_to_generate):
        seed = seed**2
        str_seed = str(seed)
        if (len(str_seed) < num_digits*2):
            diff = num_digits*2 - len(str_seed)
            str_seed = ('0'*diff) + str_seed
        hn = num_digits/2
        seed = int(str_seed[hn:-hn])
        print seed

main()
