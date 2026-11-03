

'''
비밀번호를 입력 받아서 입력한 비번이 8자 이상이면 
사용가능한 비번 입니다

그렇지 않으면 , 사용 불가

를 출력하는 간단한 프로그래밍 
 hint:len()


'''

input_pwd: str = input("비밀번호를 입력하세요: ")


if len(input_password) >= 8:
    print("사용가능한 비밀번호 입니다")
else:
    print("사용 불가 입니다")