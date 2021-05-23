#모듈 전체를 import 해올 때는
import mod

#모듈에서 특정 함수를 import 해올 때는 
from mod import func

#mod1.py와 hello.py가 있을 때
#모듈을 물러왔을 때 실행을 막으려면
if __name__ == "__main__": #으로 걸러준다.
  
#추가 : 이 구문은 import되었을 때는 실행하지 않고, 인터프리터로 직접 실행될 때만 if문 아래의 코드를 돌리라는 뜻임. 여기서 __name__은 인터프리터가 실행 전에 만들어 놓은 코드임.
