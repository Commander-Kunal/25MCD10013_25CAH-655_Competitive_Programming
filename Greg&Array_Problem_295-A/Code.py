n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

ops = []
for _ in range(m):
    # l, r are 1-indexed, d is the value to add
    ops.append(list(map(int, input().split())))

# Step 1: Count how many times each operation is executed
ops_diff = [0] * (m + 1)
for _ in range(k):
    x, y = map(int, input().split())
    ops_diff[x-1] += 1
    if y < m:
        ops_diff[y] -= 1

# Convert ops_diff to actual counts via prefix sum
ops_count = [0] * m
current_count = 0
for i in range(m):
    current_count += ops_diff[i]
    ops_count[i] = current_count

# We create a difference array of size n+1 to handle range updates
diff_arr = [0] * (n + 1)

# Initialize the difference array with the original values
diff_arr[0] = arr[0]
for i in range(1, n):
    diff_arr[i] = arr[i] - arr[i-1]

# Apply each operation multiplied by its execution count
for i in range(m):
    l, r, d = ops[i]
    total_add = d * ops_count[i]
    diff_arr[l-1] += total_add
    if r < n:
        diff_arr[r] -= total_add

# Step 3: Reconstruct the final array using prefix sums
final_arr = [0] * n
current_val = 0
for i in range(n):
    current_val += diff_arr[i]
    final_arr[i] = current_val

print(*(final_arr))
