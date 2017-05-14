import sys

def erase(times, file):
    if times % 2 == 1:
        for i in range(len(file)):
            if file[i] == "0":
                file[i] = "1"
            else:
                file[i] = "0"

    return file

def main():
    times = int(sys.stdin.readline().strip())
    before = list(sys.stdin.readline().strip())
    after = list(sys.stdin.readline().strip())
    
    if times % 2 == 0 and before == after:
        print("Deletion succeeded")
    elif times % 2 == 1 and erase(times, before) == after:
        print("Deletion succeeded")
    else:
        print("Deletion failed")

main()
