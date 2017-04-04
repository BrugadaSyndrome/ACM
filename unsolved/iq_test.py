import sys

def main():

    tests = int(sys.stdin.readline().strip())

    for t in range(tests):
        nums = sys.stdin.readline().strip().split()
        seq_len = int(nums[0])
        nums = nums[1:]
        print nums

        for n in range(len(nums)):
            S = 0
            for d in range(1, 4, 1):
                if (n-d > 0):
                    print nums[n-d], '+',
                    S += int(nums[n-d])
            print '=', S
            
        print
        print
              
main()
