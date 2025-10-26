def PrimeList(N):
    if N < 2:
        return ""
    
    # 创建一个布尔列表，标记数字是否为质数
    is_prime = [True] * N
    is_prime[0] = False
    if N > 1:
        is_prime[1] = False
    
    # 使用筛法找出所有质数
    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            # 标记i的所有倍数为非质数
            for j in range(i*i, N, i):
                is_prime[j] = False
    
    # 收集所有质数
    primes = []
    for i in range(2, N):
        if is_prime[i]:
            primes.append(str(i))
    
    # 返回以空格分隔的质数字符串
    return " ".join(primes)
