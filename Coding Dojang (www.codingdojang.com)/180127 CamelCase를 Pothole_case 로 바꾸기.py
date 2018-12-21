# 파이썬과 같은 몇몇 프로그래밍 언어는 Pothole_case 를 더 선호하는 언어라고 합니다.
# #
# # Example:
# #
# # codingDojang --> coding_dojang
# #
# # numGoat30 --> num_goat_3_0
# #
# # 위 보기와 같이 CameleCase를 Pothole_case 로 바꾸는 함수를 만들어요!
# #
# # 출처: UT past test


char = "CodingDojang"
new=char[0]
for ch in char[1:] :
    if ch.islower() : new = new + ch
    elif ch.isupper() : new = new + "_" + ch.lower() # 함수뒤에는 꼭 () !!!!!!!!!!!!!
    else : new = new+ "_" + ch
print(new)