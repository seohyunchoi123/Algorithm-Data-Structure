# 일전에 뭐 게임 회사에서 본 간단한 퀴즈 테스트 입니다.
#
# 0~9까지의 문자로 된 숫자를 입력 받았을 때, 이 입력 값이 0~9까지의 숫자가 각각 한 번 씩만 사용된 것인지 확인하는 함수를 구하시오.
#
# sample inputs: 0123456789 01234 01234567890 6789012345 012322456789 sample outputs: true false false true false

arr = input("숫자열을 입력하세요 :" )

s = arr.split(" ")
for seg in s:
    if len(seg) != len(set(seg)) : print("false")
    else : print("true") # set하면 반복된건 알아서 지워진다 !!!!!!!!!!!!!!!!!!!!!!!! 존나 중요다
        # 헐 두번쨰가 false 엿다 그니가 0~9까지 모두 한번씩은 사용되어야한다는뜻이었다. 안쓰여도 false