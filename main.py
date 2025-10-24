def PrimeList(N):
    """
    返回小于 N 的所有质数，以空格分隔
    参数：N - 正整数
    返回：str - 包含所有小于 N 的质数的字符串，空格分隔
    """
    if N <= 2:
        return ""
    
    # 初始化标记数组，全部设为True
    is_prime = [True] * N
    is_prime[0] = is_prime[1] = False
    
    # 埃拉托斯特尼筛法
    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            # 将i的倍数标记为非质数
            for j in range(i*i, N, i):
                is_prime[j] = False
    
    # 收集所有质数
    primes = [str(i) for i in range(2, N) if is_prime[i]]
    
    # 用空格连接，末尾无空格
    return " ".join(primes)
