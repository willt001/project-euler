from typing import List
from collections import defaultdict


def get_primes(n: int) -> List[int]:
    sieve = [1] * (n + 1)
    sieve[0], sieve[1] = 0, 0
    for i in range(int(n**0.5)):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0
    return [i for i, is_prime in enumerate(sieve) if is_prime]

def get_masked_numbers(num: int) -> List[str]:
    num = str(num)
    n = len(num)
    result = []
    for bitmask in range(2 ** n):
        combo = ''
        replaced = set()
        for i in range(n):
            if (bitmask >> i) & 1:
                combo += '*'
                replaced.add(num[i])
            else:
                combo += num[i]
        if len(replaced) == 1:
            result.append(combo)
    return result

def k_prime_families(k: int) -> str:
    primes = get_primes(999999)
    combo_counter = defaultdict(int)
    result = []
    for prime in primes:
        combos = get_masked_numbers(prime)
        for combo in combos:
            combo_counter[combo] += 1
            if combo_counter[combo] == k:
                result.append(combo)
    return result

if __name__ == "__main__":
    masked = k_prime_families(8)[0]
    primes = set(get_primes(999999))
    for digit in '123456789':
        if int(masked.replace('*', digit)) in primes:
            print(int(masked.replace('*', digit)))