n = int(input())

for i in range(n):  # i는 0부터 n-1까지 증가
    for _ in range(i):  # 공백 출력
        print(" ", end=" ")

    for _ in range(n*2-1 - i*2):  # '*' 개수 점점 감소
        print("*", end=" ")

    print()  # 줄 바꿈
