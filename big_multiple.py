n = int(input())

output = list()
for i in range(1, n+1):
    for j in range(1, n+1) :
        print(i * j, end="")
    print()