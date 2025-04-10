# 입력 받기
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.reverse()  # 수열 뒤집기

# 쿼리 처리
for _ in range(m):
    a, b = map(int, input().split())
    
    # 1-based index를 0-based로 변경
    total = sum(arr[a-1:b])
    print(total)
