


# 임의의 숫자를 입력 받아서 입력한 수가 양수 이면 양수 입니다를 출력하고
# 양수가 아니면 양수가 아닙니다 라고 출력하고 싶다면 (양자택일의 코드 블럭 )


input_num: int = int(input("임의의 숫자입력:"))

# 만일 input_num 이 0보다 크다면 (비교연산의 결과는 boole)
if(input_num > 0):
    print("양수입니다")

# if( not(input_num > 0)):
# if( input_num <=0):
if((input_num > 0) ==False):
    print("양수가 아닙니다")

print("-------------------")
# 로직이 만일 양자 택일 이라면 if~else 블럭을 만들면 된다

# 만일 input_num이 0보다 크다면 
if(input_num > 0):
   print("양수입니다")
else: # 그렇지 않다면 
   print("양수가 아닙니다")


print("종료 됩니다")