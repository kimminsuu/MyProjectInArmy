#모듈 전체를 import 해올 때는
import mod

#모듈에서 특정 함수를 import 해올 때는 
from mod import func

#mod1.py와 hello.py가 있을 때
#모듈을 물러왔을 때 실행을 막으려면
if __name__ == "__main__": #으로 걸러준다.
