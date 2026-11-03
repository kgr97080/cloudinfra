# 임의의 숫자를 입력 받아서 입력한 수가 양수 이면 양수 입니다를 출력하고자 한다면 ???

input_num: int = int(input("임의의 숫자입력:"))

# 만일 input_num 이 0보다 크다면 (비교연산의 결과는 boole)
if(input_num > 0):
    print(f"입력한 숫자 {input_num}은 양수 입니다.")


print("종료 됩니다")