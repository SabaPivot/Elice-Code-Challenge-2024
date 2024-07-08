n = "34132"
n = [int(d) for d in n]
i = len(n) - 2

while i >= 0 and n[i] > n[i + 1]:
    i -= 1

j = len(n) - 1

while n[i] >= n[j]:
    j -= 1
n[i], n[j] = n[j], n[i]

left = n[:i+1]
right = n[i+1:]
right.reverse()

print("".join(map(str, left + right)))