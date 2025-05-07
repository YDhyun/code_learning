#좀더 코드를 간략히 해보기!
def main():

    standard = [1,1,2,2,2,8]
    chess = input().split(' ')
    
    for i in range(len(chess)):
        print(f'{standard[i] - int(chess[i])}',end=" ")

if __name__=="__main__":
    main()