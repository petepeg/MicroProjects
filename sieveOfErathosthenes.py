from math import isqrt


def primes_less_than(n: int) -> list[int]:
    if n <= 2:
        return []
    n = n+1  # compensating for 0
    primes = [True for i in range(n)]  # init list of Trues
    primes[0] = False  # 0 is not prime
    primes[1] = False  # 1 is not prime
    # limit range to sqrt of n since anything with a perfect sqrt will be removed
    for i in range(2, isqrt(n)):
        if primes[i]:
            # start at i*i since all previous will have been removed already
            for j in range(i*i, n, i):
                primes[j] = False

    # Filter out the Trues return list of indices
    return [i for i in range(n) if primes[i]]


if __name__ == '__main__':
    print(primes_less_than(100))
