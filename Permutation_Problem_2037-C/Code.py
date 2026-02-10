t = int(input())

for _ in range(t):
    n = int(input())

    if n <= 4:
        print(-1)
        continue

    ans = []

    for i in range(2, n + 1, 2):
        if i != 4:
            ans.append(i)

    ans.append(4)

    ans.extend([5, 1, 3])

    for i in range(7, n + 1, 2):
        ans.append(i)

    print(*ans)
