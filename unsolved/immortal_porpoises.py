import sys
import math

def mod_pow(base, exponent, modulus):
    if (modulus == 1):
        return 0
    result = 1
    base = base % modulus
    while exponent > 0:
        if (exponent % 2 == 1):
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

def Binet(N):
    phi = (1 + 5 ** 0.5) / 2
    # Best bet
    A = mod_pow(phi, N, 1000000000)
    B = mod_pow(-phi, -N, 1000000000)

    # Correct but no way to mod it...
    # Overflow Error when caluclating without mod
    #A = pow(phi, N)
    #B = pow(-1*phi, -N)
    return (A - B) / 5 ** 0.5

def main():
    cases = int(sys.stdin.readline().strip())
    
    for c in range(cases):
        K, Y = sys.stdin.readline().strip().split()
        K = int(K)
        Y = int(Y)
        print K, int(Binet(Y)) #fib(1, 1, 3, Y)
        print '====='

main()
