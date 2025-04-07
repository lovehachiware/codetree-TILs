n = int(input())  # 숫자의 개수 입력받기
arr = list(map(int, input().split()))  # 숫자 리스트 입력받기

for i in range(n - 1, -1, -1):  # n-1부터 0까지 거꾸로 가는 반복문
    if arr[i] % 2 == 0:  # 짝수인지 확인
        print(arr[i], end=' ')  # 줄바꿈 없이 공백으로 출력
