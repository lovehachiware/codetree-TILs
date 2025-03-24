n = int(input())

for i in range(1, n+1):
    for _ in range(n-i):
        print(" ",end = "")
    for _ in range(i):
        print("*", end = " ")
    print()

for i in range(n,0,-1):
    for _ in range (n-i+1):
        print(" ",end="")
    for _ in range (i-1):
        print("*",end= " ")
    print()