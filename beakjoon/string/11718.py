# 입력 받은 대로 출력하는 프로그램을 작성하시오.

def main():
    # while 문으로 반복 수행하는 작업
    while True:
        # try - excpet 문 생각해보자!
        try:
            a = input()
            print(a)
        except:
            break

if __name__=="__main__":
    main()