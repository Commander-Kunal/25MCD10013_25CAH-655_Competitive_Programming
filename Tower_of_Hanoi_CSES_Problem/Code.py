n = int(input())

moves = []

def hanoi(n, a, b, c):
    if n == 0:
        return

    hanoi(n-1, a, c, b)
    moves.append((a, c))
    hanoi(n-1, b, a, c)

hanoi(n, 1, 2, 3)

print(len(moves))
for x, y in moves:
    print(x, y)
