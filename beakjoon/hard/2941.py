"""
예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.

č → c= , ć  → c- , dž → dz= , đ → d- , lj → lj, nj → nj , š → s= , ž → z=

"""

def main():
    list = ['c=','c-','dz=','d-','lj','nj','s=','z=']
    count = 0
    content = input()
    for symbol in list:
        content = content.replace(symbol,"*")

    print(len(content))

if __name__=="__main__":
    main()

# 처음 문제 해결 접근 방법으로 반복문을 이용해 검사하는 것을 수행하려고 함
# 하지만, for char in content: 를 사용하면 한글자만 처리하기 때문에 문제의 조건인 크로아티아 알파벳을 인식할 수 없다.
# replace를 이용해 크로아티아 알파벳을 특정 기호로 변환시킨 후 해당 문자열의 크기를 구하면 해결가능하다.