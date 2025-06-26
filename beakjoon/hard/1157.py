"""
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
단, 대문자와 소문자를 구분하지 않는다.
"""

def main():
    word = input().lower()
    char_count = {}
    
    # 반복문 검사를 통해 알파벳 횟수 검사
    for char in word:
        # 중복했을 때 추가
        if char in char_count:
            char_count[char] += 1
        # 초기 존재할 때 입력 값
        else :
            char_count[char] = 1

    Maxium_count = max(char_count.values())
    Maxium_common = []

    # char_count.items()로 (문자, 개수) 쌍을 반복
    for char,cnt in char_count.items():
        if cnt == Maxium_count:
            Maxium_common.append(char)

    if len(Maxium_common) > 1:
        print("?")
    else :
        print(Maxium_common[0].upper())

if __name__=="__main__":
    main()