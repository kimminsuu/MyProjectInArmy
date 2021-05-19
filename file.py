f=open("새파일.txt", 'w', encoding = "UTF-8")
for i in range(1,11):
  data = "%d번째 줄입니다.\n" %i
  f.write(data)
f.close()

#open()함수의 앞쪽엔 주소, 두번째는 읽기(r), 쓰기(w) 등, encoding은 어떤 문자로 할건지
