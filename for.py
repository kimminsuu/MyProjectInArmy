for i in range(2,10):
  for j in range(1,10):
    print(i*j, end=" ")
  print('')
#이렇게 하면 구구단처럼 출력되는데 여기서 알아야될 것.
#print()구문에는 기본적으로 end='\n'이 내포되어있는데 print가 끝나면 자동적으로 계행이 됨. 근데 end를 " "로 바꿔주면 '\n'이 실행되지 않고
#바로 뒤에 커서가 오게 됨. 그래서 밑에 print('')을 줘서 계행을 시켜주는것임.

result = [num*3 for num in a if num % 2 == 0]#과

result = []
for num in a:
  if num%2 ==0:
    result.append(num*3)
#이 같은 구문임.
