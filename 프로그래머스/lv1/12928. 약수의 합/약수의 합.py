def solution(n):
    answer = 0
    small_n = int(n ** (1/2))
    # small_n 이하의 자연수 중에 n의 약수인 자연수
    # if: small_n이 제곱근인 자연수라면(즉 약수의 갯수가 홀수일 경우) small_n한번 빼기
    for num in range(1, small_n + 1):
        if n % num == 0:
            ber = n / num
            answer += num + ber
            if num == ber:
                answer -= num
    return answer
