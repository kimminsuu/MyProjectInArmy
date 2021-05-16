score = 70
if score >= 60:
    message = "success"
else:
    message = "failure"

print(message)

#조건부 표현식 : 성공할 때의 조건 먼저 쓰고 뒤에 실패할 때의 실행
message1 = "success" if score >=60 else "failure"
print(message1)
