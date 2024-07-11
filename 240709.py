n, m = map(int, (input().split()))
arr = list(map(int, input().strip().split()))
arr_i_j_k = []
for _ in range(m):
    arr_i_j_k.append(list(map(int, (input().split()))))
arr_i_j_k = arr_i_j_k[::-1]

while m > 0:
    i, j, k = arr_i_j_k[m - 1]
    arr_temp = arr.copy()
    arr_temp[i - 1:j] = sorted(arr_temp[i - 1:j])
    print(arr_temp[i - 1 + k - 1])
    m -= 1
