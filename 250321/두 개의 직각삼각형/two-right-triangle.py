n = int(input())

for i in range(n):
    stars = n - i  # 왼쪽 별 개수
    spaces = i * 2  # 가운데 공백 개수
    
    print("*" * stars + " " * spaces + "*" * stars)
