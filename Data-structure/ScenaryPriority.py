from collections import deque

# 关系图,key是人名，value是这个人的朋友
graph = {
	'you':['alice', 'bob', 'claire'],
	'bob': ['anuj', 'peggy'],
	'alice': ['peggy'],
	'claire': ['thom', 'jonny'],
	'anuj': [],
	'peggy': [],
	'thom': [],
	'jonny': []
}

def search(name):
	search_queue = deque()
	search_queue += graph[name]
	searched = []  # 记录搜索过的人

	while search_queue:
		person = search_queue.popleft()
		if person not in searched:
			if person_is_seller(person):
				print('{} is a mango seller'.format(person))
				return True
			else:
				search_queue += graph[person]  # 将person的朋友加入到队列中

		searched.append(person)

	return False

def person_is_seller(name):
	'''stub代码'''
	return name[-1] == 'm'

if __name__ == '__main__':
	search('you')