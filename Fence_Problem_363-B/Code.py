n, k = map(int, input().split())
h = list(map(int, input().split()))

curr = sum(h[:k])
mn = curr
idx = 0

for i in range(k, n):
    curr += h[i]
    curr -= h[i-k]

    if curr < mn:
        mn = curr
        idx = i - k + 1

print(idx + 1)
