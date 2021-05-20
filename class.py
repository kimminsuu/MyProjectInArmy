class FourCal:
  def __init__(self,first,second):
    self.first = first
    self.second = second
  def setdata(self, first, second):
    self.first = first
    self.second = second
  def add(self):
    result = self.first + self.second
    return result
    
#여기서 self는 a를 , first와 second는 setdata의 인수들
a = FourCal(1,2) #__init__을 써줬을 때는 생성자를 형식에 맞춰 써줌
a.setdata(1,2)
print(a.first)
print(a.second)
print(a.add())
