# 문제 설명
# n명이 입국심사를 위해 줄을 서서 기다리고 있습니다. 각 입국심사대에 있는 심사관마다 심사하는데 걸리는 시간은 다릅니다.
#
# 처음에 모든 심사대는 비어있습니다. 한 심사대에서는 동시에 한 명만 심사를 할 수 있습니다. 가장 앞에 서 있는 사람은 비어 있는 심사대로 가서 심사를 받을 수 있습니다. 하지만 더 빨리 끝나는 심사대가 있으면 기다렸다가 그곳으로 가서 심사를 받을 수도 있습니다.
#
# 모든 사람이 심사를 받는데 걸리는 시간을 최소로 하고 싶습니다.
#
# 입국심사를 기다리는 사람 수 n, 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times가 매개변수로 주어질 때, 모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 입국심사를 기다리는 사람은 1명 이상 1,000,000,000명 이하입니다.
# 각 심사관이 한 명을 심사하는데 걸리는 시간은 1분 이상 1,000,000,000분 이하입니다.
# 심사관은 1명 이상 100,000명 이하입니다.
# 입출력 예
# n	times	return
# 6	[7, 10]	28

# def solution(n, times):
#     board = [0] * len(times)
#     min_idx = 0
#     for i in range(n):
#         min_value = 1000000000 ** 2
#         for idx, time in enumerate(times):
#             if min_value > (board[idx] + 1) * time:
#                 min_value = (board[idx] + 1) * time
#                 min_idx = idx
#         board[min_idx] += 1
#
#     ans = []
#     for i in range(len(times)):
#         ans.append(times[i] * board[i])
#     return max(ans)

def cal_n(num, times): # 걸린 총 시간을 기반으로 n 값을 구하기
    ans = 0
    is_minimum = False # 걸린 총 시간이 구해진 n의 최솟값인지 여부
    for time in times:
        ans += num//time # 이 방법이 있었자나 왠 for문을 돌리고잇어??... 하나배웠다!!
        if num % time == 0:
            is_minimum = True
    return ans, is_minimum


def solution(n, times):
    start = 0
    end = max(times) * n
    while True:
        mid = (start + end) // 2
        mid_n, is_minimum = cal_n(mid, times)
        # start == mid or end == mid 경우는 반드시 체크해줘야함 !! 아니면 무한루프돌아
        if start == mid:
            mid += 1
            break
        elif end == mid:
            mid -= 1
            break

        if n > mid_n:
            start = mid
        elif n < mid_n or not is_minimum:
            end = mid
        else:
            break
    return mid


# Time Complexity: log(n)
# Space Complexity: 1