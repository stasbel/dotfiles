import math


class DisjointSet:
    _disjoint_set = list()

    def __init__(self, init_arr):
        self._disjoint_set = []
        if init_arr:
            for item in list(set(init_arr)):
                self._disjoint_set.append([item])

    def _find_index(self, elem):
        for item in self._disjoint_set:
            if elem in item:
                return self._disjoint_set.index(item)
        return None

    def find(self, elem):
        for item in self._disjoint_set:
            if elem in item:
                return self._disjoint_set[self._disjoint_set.index(item)]
        return None

    def union(self, elem1, elem2):
        index_elem1 = self._find_index(elem1)
        index_elem2 = self._find_index(elem2)
        if index_elem1 != index_elem2 and index_elem1 is not None and index_elem2 is not None:
            self._disjoint_set[index_elem2] = self._disjoint_set[index_elem2] + \
                                              self._disjoint_set[index_elem1]
            del self._disjoint_set[index_elem1]
        return self._disjoint_set

    def get(self):
        return self._disjoint_set


def sieve(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    for i in range(2, n + 1):
        if prime[i]:
            if i ** 2 <= n:
                for j in range(i ** 2, n + 1, i):
                    prime[j] = False

    return prime


def connectedCities(n, g, originCities, destinationCities):
    q = int(math.sqrt(n)) + 1
    primes = sieve(q)
    primes = [i for i in range(len(primes)) if primes[i]]
    primes1 = [1] + primes

    dsu = DisjointSet([i for i in range(1, n + 1)])

    def add(a, b):
        if a // b > g:
            dsu.union(a, a // b)
            return True
        return False

    # for prime in primes:
    #     k = 1
    #     while prime * k <= n and k <= prime:
    #         i = k * prime
    #         add(i, prime)
    #         add(i, i // prime)
    #         j = (prime - k) * prime
    #         if j > 0:
    #             add(j, prime)
    #             add(j, j // prime)
    #         k += 1
    #
    # for i in range(1, n + 1):
    #     add(i, i)

    for i in range(1, n + 1):
        for prime in primes1:
            if prime ** 2 > i:
                break

            if i % prime != 0:
                continue

            add(i, prime)  # gcd is: i // prime
            add(i, i // prime)  # gcd is: prime

        add(i, i)

    paths = []
    for o, d in zip(originCities, destinationCities):
        paths.append(int(dsu.find(o) == dsu.find(d)))

    return paths


def main():
    print(connectedCities(6, 0, [1, 4, 3, 6], [3, 6, 2, 5]))
    print(connectedCities(6, 1, [1, 2, 4, 6], [3, 3, 3, 4]))
    print(connectedCities(200000, 12, [], []))


if __name__ == '__main__':
    main()
