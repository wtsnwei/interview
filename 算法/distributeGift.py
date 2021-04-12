dictGiftIn = {'Jack':'apple','Peter':'beer','Tom':'card','Duke':'doll','Mary':'pineapple','James':'flute','Tina':'coffee'}
dictGiftOut = {}

persons = list(dictGiftIn.keys())

for p in persons:
	flag = 0 #  标记自己带来的礼物是否还未分配出去
	if p in dictGiftIn:
		flag = 1
	myGift = dictGiftIn.pop(p) #  先在未分配名单中排除该礼物
	getGift = dictGiftIn.popitem() #  随机返回并移除key-value值, 即分配礼物
	dictGiftOut[p] = getGift[1] #  已分配礼物名单
	if flag:
		dictGiftIn[p] = myGift #  如果当前礼物没有分配，则该礼物重新添到未分配名单中
 
print(dictGiftOut) #  输出礼物分配情况