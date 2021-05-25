import sys

option = sys.argv[1]

if option == '-a':
  memo = sys.argv[2]
  f = open('memo.txt','a')
  f.write(memo)
  f.write('\n')
  f.close()
  #이렇게 하면 -a "string" 이렇게 하면 memo.txt에 입력이 됨.

elif option == '-v':
  f = open('memo.txt')
  memo = f.read()
  f.close()
  print(memo)
  #이렇게 하면 -v를 입력했을 때 메모에 쓴 내용을 불러오게 됨.
  
  https://www.youtube.com/watch?v=udeQhZHx-00
