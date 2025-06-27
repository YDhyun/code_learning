"""
인하대학교 컴퓨터공학과를 졸업하기 위해서는, 전공평점이 3.3 이상이거나 졸업고사를 통과해야 한다.
그런데 아뿔싸, 치훈이는 깜빡하고 졸업고사를 응시하지 않았다는 사실을 깨달았다!
치훈이의 전공평점을 계산해주는 프로그램을 작성해보자.
전공평점은 전공과목별 (학점 X 과목평점)의 합을 학점의 총합으로 나눈 값이다.
인하대학교 컴퓨터공학과의 등급에 따른 과목평점은 다음 표와 같다.
A+ : 4.5, A0 : 4.0, B+ : 3.5, B0 : 3.0, C+ : 2.5, C0 : 2.0, D+ : 1.5, D0 : 1.0, F : 0.0

P/F 과목의 경우 등급이 P또는 F로 표시되는데, 등급이 P인 과목은 계산에서 제외해야 한다.
과연 치훈이는 무사히 졸업할 수 있을까?
"""


def main():
    # 이중 반복문을 통해 2차원 배열 생성
    grade = list()
    for i in range(20):
        grade.append(input().split(' '))

    # 학점 총계 저장 변수
    total_score = 0.0
    # 학점 수 저장 변수
    count = 0
    # 학점 변환 수행
    for i in range(20):
        if grade[i][2] == 'A+': grade[i][2] = 4.5
        elif grade[i][2] == 'A0': grade[i][2] = 4.0
        elif grade[i][2] == 'B+': grade[i][2] = 3.5
        elif grade[i][2] == 'B0': grade[i][2] = 3.0
        elif grade[i][2] == 'C+': grade[i][2] = 2.5
        elif grade[i][2] == 'C0': grade[i][2] = 2.0
        elif grade[i][2] == 'D+': grade[i][2] = 1.5
        elif grade[i][2] == 'D0': grade[i][2] = 1.0
        elif grade[i][2] == 'F': grade[i][2] = 0.0
        # P/F 과목은 계산에서 제외 시켜야한다!    
        else : 
            continue
        count += float(grade[i][1])
        total_score += float(grade[i][1]) * grade[i][2]
    
    print(total_score/count)

if __name__=="__main__":
    main()

# 입력값 받을 때 2차원 배열을 사용해야하나? 
# -> 파이썬에서 2차원 배열 선언을 할 때 얇은 복사를 방지하기 위해서 이중 반복문을 이용해서 선언하자.
# 반복문을 통해서 입력값을 받아야하나? 
# 맨 처음 접근 방식 grade = [['' for i in range(3)] for j in range(20)]
#  for cols in range(20):
#        for rows in range(3):
#   를 통해서 입력 받기  

# C언어에서는 메모리부터 할당해서 빈 상태에서 대입이 가능하지만, 
# 파이썬에서는 배열 선언할때 동적 리스트로 선언되기 때문에 빈상태에서 대입이 불가능하다!
# append() 함수를 이용해 배열에 추가하기 및 split를 통해 분할 수행
# 학점 * 과목별 점수를 수행해야된다. 이때 P일 때는 계산 무시 처리 수행하기 위해 조건문 수행
# 학점에 맞춰서 변환 수행 처리하기 
