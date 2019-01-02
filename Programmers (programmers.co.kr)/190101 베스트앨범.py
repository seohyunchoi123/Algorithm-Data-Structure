# 문제 설명
# 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.
#
# 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
# 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.
#
# 제한사항
# genres[i]는 고유번호가 i인 노래의 장르입니다.
# plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
# genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
# 장르 종류는 100개 미만입니다.
# 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
# 모든 장르는 재생된 횟수가 다릅니다.
# 입출력 예
# genres	plays	return
# [classic, pop, classic, classic, pop]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]

from collections import defaultdict


def my_sum(arr):
    sum = 0
    for element in arr:
        sum += element[1]
    return sum


def solution(genres, plays):
    answer = []
    dic = defaultdict(list)
    dic_2 = {}
    for i in range(len(genres)):
        dic[genres[i]].append((i, plays[i]))
    for key in dic.keys():
        dic[key].sort(key = lambda x: (-x[1], x[0])) # keys are the number of being played in decreasing order and then the index number in increasing order.
        dic_2[key] = my_sum(dic[key]) # calculating the total number of being played for all songs in the genre
    for key, value in sorted(dic_2.items(), key = lambda x: -x[1]):
        answer.append(dic[key][0][0])
        if len(dic[key])>=2:
            answer.append(dic[key][1][0])
    return answer

# Method to Solve : Hash
# Time Complexity : O(N)
# Space Complexity : O(N)