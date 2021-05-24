f = open('foo.txt', 'w')
try:
  #수행
  data = f.read()
  print(data)
except Exception as e:
  #여기서 Exception은 모든 예외의 부모클래스
  print(e)
finally:
  f.close()
  
#또는 exception을 잡지 않고 pass로 넘어갈 수도 있음. 한번에 여러개의 예외처리도 가능

class Bird:
  def fly(self):
    raise NotImplementedError #raise 구문으로 예외를 발생시킬 수도 있음. 보통 class를 변형해서 쓰게 하는 것을 의도하고 raise를 쓰는데
    #변형할 것을 강제하는 것임.
    
class Eagle(Bird):
  def fly(Self):
    print("very fast")

eagle = Eagle()
eagle.fly()
