def PrimeList(N):
    if N <= 2:
        return ""

    is_prime = [True] * N
    is_prime[0] = False
    is_prime[1] = False
    
    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, N, i):
                is_prime[j] = False
    
    primes = []
    for i in range(2, N):
        if is_prime[i]:
            primes.append(str(i))
    
    return " ".join(primes)
