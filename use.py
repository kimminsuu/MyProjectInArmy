#탭을 4개의 공백으로 바꾸기\
#터미널에서 처음 입력시 python use.p a.txt b.txt #argv[1] = a.txt, argv[2] = b.txt
import sys
src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read() #전부 읽어서 tab_content 변수에 넣음
f.close()

space_content = tab_content.replace("\t"," "*4) #space_content는 tab_con에서 tab을 space*4로만 바꾼 변수임
print(space_content)

f = open(dst, 'w')
f.write(space_content)
f.close() #space_content를 dst에 써줌.
