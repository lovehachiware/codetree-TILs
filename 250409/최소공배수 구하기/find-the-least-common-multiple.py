# 최대공약수 함수 (GCD)
def find_gcd(n, m):
    gcd = 0
    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            gcd = i
    return gcd

# 최소공배수 함수 (LCM)
def find_lcm(n, m):
    gcd = find_gcd(n, m)  # 먼저 최대공약수를 구하고
    lcm = (n * m) // gcd  # 공식을 사용해서 최소공배수를 구함
    return lcm

# 입력 받기
n, m = map(int, input().split())

# 결과 출력

print(find_lcm(n, m))
