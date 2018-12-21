# 111번 문제 "욕심쟁이 판다"와 연관된 문제입니다.
#
# 임의의 수열 S가 주어졌을 때, S의 일부 항(연속될 필요는 없다)을 원래 순서대로 나열해 얻을 수 있는 수열을 S의 부분수열(Subsequence)이라 한다.
#
# 예를 들어 [12, 7, 10, 9]는 [12, 5, 7, 3, 10, 9] 의 부분수열이다.
#
# 또한 어떤 부분수열에서 앞의 숫자보다 뒤의 숫자가 항상 더 클 때,
#
# 즉 부분수열 [x1, x2, ..., xn]에서 모든 i (1 <= i < n)에 대해 xi < x(i+1) 이면 이를 증가하는 부분수열(Increasing subsequence)이라고 한다.
#
# 예를 들어 [12, 7, 10, 9]는 [12, 5, 7, 3, 10, 9]의 부분수열이지만 증가 수열이 아니고, [5, 7, 10]은 [12, 5, 7, 3, 10, 9]의 증가하는 부분수열이다.
#
# 어떤 수열이 입력으로 주어질 때, 이 수열의 증가하는 부분수열 중 가장 긴 부분수열의 길이를 출력하시오.
#
# 입력: 수열의 길이와 수열을 이루는 음이 아닌 정수들이 한 줄에 주어진다.
#
# 9 10 20 40 25 20 50 30 70 85
# 출력: 위 입력의 LIS 중 하나는 [9, 10, 20, 40, 50, 70, 85] 이다.
#
# 답 : 7

num_list=[9,10,20,40,25,20,50,30,70,85]

while True :
    removing_index = []
    length = len(num_list)-1
    for i in range(length):
        if num_list[i] >= num_list[i+1] :
            removing_index.append(i)
    t = set(range(len(num_list))) - set(removing_index)
    num_list = np.array(num_list)[list(t)]
    if removing_index == [] :
        break
print (num_list)