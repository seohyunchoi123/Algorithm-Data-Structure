n = int(input())
basket =[]
for _ in range(n):
    basket.append(int(input()))
# 오름차순 1,2,3,4,5
basket = [sorted(basket[(2*i):(2*i+2)]) for i in range(len(basket)//2+1)]
while True:
    new_basket =[]
    small_basket=[]
    for idx in range(len(basket)//2+1):
        ele_1 = basket[2 * idx]
        ele_2 = basket[2 * idx+1]
        idx_1 =0;idx_2=0
        for _ in range(len(ele_1)**2):
            if ele_1[idx_1]>ele_2[idx_2]:
                small_basket.append(ele_2[idx_2])
                idx_2+=1
                if idx_2 >(len(ele_2)-1):
            else:
                small_basket.append(ele_1[idx_1])
                idx_1+=1
            if len(small_basket) == (len(ele_1) + len(ele_2)):
                break
        new_basket.append(small_basket)
    basket = new_basket.copy()
    if len(basket) ==n:
        break
for t in basket:
    print(t)



for t in basket:
    print(t)

set([1,2,3]).