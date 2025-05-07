'''
전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다.
숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.
숫자 1을 걸려면 총 2초가 필요하다. 
1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.
상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다.
즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.
할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오
'''
def main():
    #단어 입력
    dial = input().strip().upper()
    #결과값 저장 변수 선언
    result = 0
    # 기존 문제를 풀었을 때(5622.py) 인덱스 값을 이용해 해당 인덱스의 존재하는 값을 비교하는 방법으로 풀었음
    # 이번에는 직접 문자를 선회하는 방법으로 코드를 작성해보겠다.
    for ch in dial:
        if ch in 'ABC':
            result += 3
        elif ch in 'DEF':
            result += 4 
        elif ch in 'GHI':
            result += 5
        elif ch in 'JKL':
            result += 6
        elif ch in 'MNO':
            result += 7
        elif ch in 'PQRS':
            result += 8
        elif ch in 'TUV':
            result += 9
        elif ch in 'WXYZ':
            result += 10
        else:
            print("잘못된 입력입니다.")
        
       
    print(result)


if __name__ =="__main__":
    main()