from sys import stdin

input = stdin.readline
mod = int(1e9) + 7


def MatrixProduct(arr1: list[list[int]], arr2: list[list[int]]):
    answer = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                answer[i][j] += arr1[i][k] * arr2[k][j]
            # answer[i][j] %= mod
    return answer


def fibo(n: int):
    if n < 1:
        return 0
    ans = [[1, 0], [0, 1]]
    a = [[1, 1], [1, 0]]

    while n > 0:
        if n % 2 == 1:
            ans = MatrixProduct(ans, a)
        a = MatrixProduct(a, a)
        n //= 2
    return ans[0][1]

def binarySearch(n: int):
    start, end = 0, 100_000
    while start <= end:
        mid = (start + end) // 2
        tmp = fibo(mid)
        if tmp > n:
            end = mid - 1
        else:
            start = mid + 1
    return end

for _ in range(int(input())):
    n = int(input())
    print(binarySearch(n))
