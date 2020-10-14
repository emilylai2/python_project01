#不可用queue.py 因為系統內部有這個程式

#創建資料隊伍
from multiprocessing import*
from random import randint
from time import*

q=Queue(5)#最大長度五

def handle():
	for i in range(6): 
		x=randint(1,33)
		q.put(x)#等於放六個數字進入隊伍
	q.put(randint(1,16))
	
def request():
	while True:
		l=[]
		for i in range(6):
			l.append(q.get())
		l.sort()	
		l.append(q.get())#等排隊好再打印

p1=Process(target=handle)
p2=Process(target=request)
p1.start()
p2.start()
p1.join()
p2.join()
