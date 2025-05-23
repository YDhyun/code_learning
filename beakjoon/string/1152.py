""" 
    문제 : 1152
    영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 
    이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오. 
    단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.
"""
# 기존 input()은 사용자 입력을 그대로 가져오는 반면, 
# input.strip()는 앞뒤 공백을 제거해서 가져온다.
string1 = input().strip()

# 공백으로 단어 분리
string2 = string1.split()

# 길이 출력
print(len(string2))
