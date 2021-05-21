class FourCal:
  def __init__(self, first, second):
    self.first = first
    self.second = second
  def setdata(self, first, second):
    self.first = first
    self.second = second
  def add(self):
    result = self.first + self.second
  def sub(self):
    result = self.first - self.second
  def mul(self):
    result = self.first * self.second
  def div(self):
    result = self.first / self.second
  
class SafeFourCal(FourCal): #FourCal을 상속받으면 FourCal 클래스의 기능을 쓸 수 있음.
  def div(self):
    if self.second == 0:
      return 0
    else:
      return self.first / self.second

a = SafeFourCal(4, 2)
print(a.div())
#다음과 같이 상속한 클래스에 같은 함수를 오버라이딩할 시 상속한 클래스의 함수로 
