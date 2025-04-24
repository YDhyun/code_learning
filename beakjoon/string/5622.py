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
    dial = input("단어를 입력하세요 : ").strip().upper()
    result = 0
    i = 0
    for i in range(len(dial)):
        time = 2
        # 파이썬에서 or 논리연산자는 or로 사용된다. 
        if (dial[i]=='A' or dial[i]=='B' or dial[i]=='C'):
            time += 1
            result += time
        elif(dial[i]=='D' or dial[i]=='E' or dial[i]=='F'):
            time += 2
            result += time
        elif(dial[i]=='G' or dial[i]=='H' or dial[i]=='I'):
            time += 3
            result += time
        elif(dial[i]=='J' or dial[i]=='K' or dial[i]=='L'):
            time += 4
            result += time
        elif(dial[i]=='M' or dial[i]=='N' or dial[i]=='O'):
            time += 5
            result += time
        elif(dial[i]=='P' or dial[i]=='Q' or dial[i]=='R' or dial[i]=='S'):
            time += 6
            result += time
        elif(dial[i]=='T' or dial[i]=='U' or dial[i]=='V'):
            time += 7
            result += time
        elif(dial[i]=='W' or dial[i]=='X' or dial[i]=='Y' or dial[i]=='Z'):
            time += 8
            result += time
        else:
            print("잘못된 문자열을 입력했습니다.")
            break
    print(result)


if __name__ =="__main__":
    main()