f=open("새파일.txt", 'w', encoding = "UTF-8")
for i in range(1,11):
  data = "%d번째 줄입니다.\n" %i
  f.write(data)
f.close()

#open()함수의 앞쪽엔 주소, 두번째는 읽기(r), 쓰기(w) 등, encoding은 어떤 문자로 할건지

#새파일.txt에 있는 줄을 line 변수에 넣어서 받아옴
f=open("C:/Python/새파일.txt", 'r')
line = f.readline()
print(line)
f.close()

#새파일.txt에 있는 문장들을 line변수로 받아서 NULL을 받아 break될 때까지 받아옴.
f = open("C:/Python/새파일.txt", 'r')
while True:
  line = f.readline()
  if not line: break
  print(line)
f.close()
