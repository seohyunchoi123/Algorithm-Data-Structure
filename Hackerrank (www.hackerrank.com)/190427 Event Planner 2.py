n = int(input())
m = int(input())
quantity = []
price = []
for _ in range(m):
    quantity.append(float(input()))
_ = input()
for _ in range(m):
    price.append(float(input()))

dic = []
for i in range(len(quantity)):
    if price[i] > 0:
        dic.append((quantity[i], price[i]))
dic = sorted(dic, key=lambda x : x[0])

def solution(n, dic):
    if len(dic) == 1:
        return dic[0][1]
    elif n < dic[0][0]:
        small, large = dic[0], dic[1]
        slope = (large[1] - small[1])/(large[0] - small[0])
        result = (n - small[0]) * slope + small[1]
    elif n > dic[-1][0]:
        small, large = dic[-2], dic[-1]
        slope = (large[1] - small[1]) / (large[0] - small[0])
        result = (n - large[0]) * slope + large[1]
    else:
        for i in range(len(dic)):
            if dic[i][0] == n:
                return dic[i][1]
        for i in range(len(dic)):
            if n > dic[i][0]:
                large = dic[i+1]
                small = dic[i]
                slope = (large[1] - small[1]) / (large[0] - small[0])
                result = (n - large[0]) * slope + large[1]
    if result > 0:
        return  round(result * 100 + 0.1)/100
    else:
        return round(result * 100 - 0.1) / 100


print(solution(n,dic))
