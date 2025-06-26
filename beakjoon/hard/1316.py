"""
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 
예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만,
aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.
"""

def main():
    line = int(input())
    word = list()
    # 입력 받을 단어
    for i in range(line):
        word.append(input())
    # 그룹 단어 수
    count = 0

    for i in range(line):
        # 검사 리스트 초기화
        check = list()
        # 참 거짓 판단
        is_check = True
        # 이전 알파벳 저장 리스트 선언
        prev = ''
        for ch in word[i]:
            # check 리스트 안에 알파벳 존재여부 파악
            if ch != prev:
                if ch in check:
                    is_check = False
                    break
                # check 리스트 안에 알파벳 추가
                check.append(ch)
                prev = ch

        # 그룹 단어일 때만 카운트
        if is_check:
            count += 1
    print(count)

if __name__=="__main__":
    main()

## 문자열을 문자 단위로 순회하여 그룹 단어 여부를 판단함
## 그룹 단어가 아닌 경우 즉시 반복문을 종료하기 위해 플래그 사용
## 이전 문자(prev)를 저장하여 연속되지 않은 같은 문자가 재등장하는 경우를 정확히 탐지
## 중복 검사용 리스트(check)에 연속이 끊긴 문자를만 기록하여 재등장 여부를 판단