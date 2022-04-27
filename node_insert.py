#노드 생성
class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

def printNodes(start) : #노드 출력
	current = start
	if current == None :
		return
	print(current.data, end=' ')
	while current.link != None :
		current = current.link
		print(current.data, end=' ')
	print()

def insertNode(findData, insertData) :	#노드 삽입
	global memory, head, current, pre

	if head.data == findData :	#첫번째 노드 삽입
		node = Node()
		node.data = insertData
		node.link = head
		head = node
		return

	current = head
	while current.link != None :	#중간 노드 삽입
		pre = current
		current = current.link
		if current.data == findData :
			node = Node()
			node.data = insertData
			node.link = current
			pre.link = node
			return

	node = Node()	#마지막 노드 삽입
	node.data = insertData
	current.link = node

#전역 변수 선언
memory = []
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

#메인코드
if __name__ == "__main__" :

	node = Node()
	node.data = dataArray[0]
	head = node
	memory.append(node)

	for data in  dataArray[1:] :
		pre = node
		node = Node()
		node.data = data
		pre.link = node
		memory.append(node)

	printNodes(head)#초기

	insertNode('다현', '화사')#insertNode(a, b) a앞에 b 삽입
	printNodes(head)

	insertNode('사나', '솔라')
	printNodes(head)

	insertNode('재남', '문별')#a라는 데이터가 없는 경우 맨 마지막 삽입
	printNodes(head)