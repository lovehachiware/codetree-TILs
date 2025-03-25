n = int(input())

for i in range(1, 2 * n + 1):  # 줄 번호: 1 ~ 6 (n = 3이면)
    if i % 2 == 1:  # 홀수 줄 → 3, 2, 1로 줄어드는 패턴
        print("* " * (n - (i // 2)))
    else:  # 짝수 줄 → 1, 2, 3로 증가하는 패턴
        print("* " * (i // 2))
