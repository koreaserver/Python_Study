import random

print("<< 사다리 게임 >>")
number = int(input("사다리 갯수를 정해주세요 : "))
ingroup = []
outgroup = []

for i in range(0, number) :
	ingroup_text = input("출발 이름을 정해주세요 : ")
	ingroup.append(ingroup_text)
	print(ingroup)
	outgroup_text = input("도착 이름을 정해주세요 : ")
	outgroup.append(outgroup_text)
	print(outgroup)

random.shuffle(outgroup)

for i in range(0, number) :
	print(ingroup[i], " -> ", outgroup[i])