t = int(input())

def max_min_char_count(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return max(freq, key=freq.get), min(freq, key=freq.get), freq
for _ in range(t):
    n = int(input())
    s = list(input())
    if n == 1:
        print(s[0])
        continue
    hcl, lcl, freq = max_min_char_count(s)
    if freq[hcl] == freq[lcl]:
        if len(freq) == 1:
            print("".join(s))
            continue
        i = 0
        j = 1
        while j < n and s[i] == s[j]:
            j += 1
    else:
        i = s.index(lcl)
        j = s.index(hcl)
    s[i] = s[j]
    print("".join(s))
