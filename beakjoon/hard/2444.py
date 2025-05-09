# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
""" 
입력 : 5
출력 
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""

def main():
    number = int(input())
    for i in range(number):
        for j in range(1,number-i):
            print(" ",end="")
        for j in range(i*2 + 1):
            print("*",end='')
        print()
    for i in range(1,number):
        for j in range(i):
            print(" ",end='')
        for j in range((number-1-i)*2 + 1):
            print("*",end='')
        print()

if __name__=="__main__":
    main()