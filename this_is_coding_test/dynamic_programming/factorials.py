def fib(n: int, memo: list[int]) -> int:
    if memo[n] == -1:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


# 피보나치 수열 [0, 1, 1, 2, 3, 5, 8]
n = 6
memo = [-1] * (n + 1)
memo[0], memo[1] = 0, 1
print(fib(n, memo))


# 풀어서 사용 (iter 구현)
def fib_iter(n: int) -> int:
    memo = [-1] * (n + 1)
    memo[0], memo[1] = 0, 1
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]


print(fib_iter(4))


def factorial(num: int) -> int:
    if num == 1:
        return 1  # 기저 조건
    return num * factorial(num - 1)


print(factorial(3))  # 3 * 2 * 1
