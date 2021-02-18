#2017.4.8
import sys

def read_room():
    w, h = sys.stdin.readline().strip().split()
    w, h = int(w), int(h)
    if w == 0 and h == 0:
        return False

    #track positions
    think, actual = [0,0],[0,0]
  
    #read moves
    num_moves = int(sys.stdin.readline().strip())
    moves = []
    for i in range(num_moves):
        moves.append(sys.stdin.readline().strip().split())

    #make moves
    for M in moves:
        step = int(M[1])
       
        if (M[0] == 'u'):
            #print("up {0}".format(step))
            #print("think {0} {1}".format(think[0], think[1]+step))
            think[1] += step
            if (actual[1] + step) > h-1:
                #print("* actual {0} {1}".format(actual[0], w-1))
                actual[1] = h-1
            else:
                #print("actual {0} {1}".format(actual[0], actual[1]+step))
                actual[1] += step

        elif (M[0] == 'd'):
            #print("down {0}".format(step))
            #print("think {0} {1}".format(think[0], think[1]-step))
            think[1] -= step
            if (actual[1] - step) < 0:
                #print("* actual {0} {1}".format(actual[0], 0))
                actual[1] = 0
            else:
                #print("actual {0} {1}".format(actual[0], actual[1]-step))
                actual[1] -= step

        elif (M[0] == 'l'):
            #print("left {0}".format(step))
            #print("think {0} {1}".format(think[0]-step, think[1]))
            think[0] -= step
            if (actual[0] - step) < 0:
                #print("* actual {0} {1}".format(0, actual[1]))
                actual[0] = 0
            else:
                #print("actual {0} {1}".format(actual[0]-step, actual[1]))
                actual[0] -= step

        elif (M[0] == 'r'):
            #print("right {0}".format(step))
            #print("think {0} {1}".format(think[0]+step, think[1]))
            think[0] += step
            if (actual[0] + step) > w-1:
                #print("* actual {0} {1}".format(h-1, actual[1]))
                actual[0] = w-1
            else:
                #print("actual {0} {1}".format(actual[0]+step, actual[1]))
                actual[0] += step

    print("Robot thinks {0} {1}".format(think[0],think[1]))
    print("Actually at {0} {1}".format(actual[0], actual[1]))
    print("")

    return True

def main():
    while True:
        more = read_room()
        if more == False:
            break

main()
