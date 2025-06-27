"""
N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.
"""
def main():
    rows, cols = map(int,input().split())

    matrix_A = list()
    matrix_B = list()
    #A 행렬에 입력값 넣기
    for i in range(rows):
        matrix_A.append(list(map(int,input().split())))
    #B 행렬에 입력값 넣기
    for i in range(rows):
        matrix_B.append(list(map(int,input().split())))
    # A+B 행렬 더하기
    for i in range(rows):
        for j in range(cols):
            print(matrix_A[i][j] + matrix_B[i][j],end=' ')
        print()



if __name__=="__main__":
    main()

# map map(func, iterable) 함수의 경우에는 iterable의 모든 원소에 func() 적용한다.
# 2개의 행렬을 선언 및 입력값 넣기 map 함수 사용하기
# 이중 반복문을 통해서 각 요소들끼리 덧셈 수행
# 덧셈 행렬 결과값도 추가 선언하기!
# 행렬 결과값을 추가 선언안하고 그냥 출력문으로 만들어도 상관없을듯하다. 
