n = int(input())
basket =[]
for _ in range(n):
    basket.append(int(input()))

for j in range(len(basket)-1):          # 오름차순을 하려면
    for i in range(j, len(basket)-1): # 여기를 range(len(basket)-1-j) 로
        if basket[i] > basket[i+1]: # 여기 등호 반대로
            pass
        else:
            basket[i], basket[i+1] = basket[i+1], basket[i]
for t in basket:
    print(t)

# n = int(input())
# basket =[]
# for _ in range(n):
#     basket.append(int(input()))
# basket = sorted(basket)
# for t in basket:
#     print(t)
