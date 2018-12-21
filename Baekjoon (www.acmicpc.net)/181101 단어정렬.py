n = int(input())
arr = []
for _ in range(51):
    arr.append([])
for _ in range(n):
    word = input()
    length = len(word)
    if word not in arr[length]:
        arr[length].append(word)

for sub_list in arr:
    for t in sorted(sub_list):
        print(t)