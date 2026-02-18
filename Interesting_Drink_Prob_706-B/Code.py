n = int(input())
x = list(map(int, input().split()))
x.sort()
q = int(input())
for _ in range(q):
    m = int(input())
    l, r = 0, n - 1
    ans = 0
    while l <= r:
        mid = l + (r-l) // 2
        if x[mid] <= m:
            ans = mid + 1
            l = mid + 1
        else:
            r = mid - 1
    print(ans)
