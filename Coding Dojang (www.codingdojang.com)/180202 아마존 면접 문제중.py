# 다음과 같은 형태의 배열을
#
# [a1,a2,a3...,an,b1,b2...bn] 다음과 같은 형태로 바꾸시오
#
# [a1,b1,a2,b2.....an,bn] 면접문제

amazon = ["a1","a2","a3","a4","a5","b1","b2","b3","b4","b5"]
amazon_final = []
index = amazon.index("b1") # index 기억 !!!

for i in range(index):
    amazon_final.append(amazon[i])
    amazon_final.append(amazon[index+i])

print(amazon_final)