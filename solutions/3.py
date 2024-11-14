def solution(num):
    i = 2
    factors = []
    while num > 1:
        while num % i == 0:
            num = num // i
            factors.append(i)
        i += 1
    return factors

print(solution(600851475143))

