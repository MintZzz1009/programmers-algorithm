def solution(n):
    answer = 0
    # n % x == 1
    # 1) n - 1 소수라면, x == n - 2
    if is_prime_number(n - 1):
        return n - 2
    # 2) n - 1 소수 아니라면, 제곱근까지 for문 돌리기
    for num in range(2, int(n - 1 ** 0.5) + 1):
        if (n - 1) % num == 0:
            return num
    

def is_prime_number(n):
    sqrt_n = n ** 0.5
    for num in range(1, int(sqrt_n + 1)):
        if n % num == 0:
            return False
    return True
