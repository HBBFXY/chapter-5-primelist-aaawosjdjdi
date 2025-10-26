def PrimeList(N):
    if N <= 2:
        return ""
    
    # 创建质数标记数组
    is_prime = [True] * N
    is_prime[0] = False
    is_prime[1] = False
    
    # 使用埃拉托斯特尼筛法
    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, N, i):
                is_prime[j] = False
    
    # 收集所有质数
    primes = []
    for i in range(2, N):
        if is_prime[i]:
            primes.append(str(i))
    
    # 返回结果
    return " ".join(primes)
