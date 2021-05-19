a=1
global b = 1
def sum(a):
  a=a+1
  b=b+1

sum(a)
print(a)
print(b)
#전역변수와 지역변수

def sum_many(*args):
  sum = 0
  for k in args:
    sum += 1
  return sum
print(sum_many(1,2,3,4,5))
#이건 배열 or 튜플 or 리스트를 지역변수로 받을 때 사용하는 방법. 더블포인터도 할당 가능

