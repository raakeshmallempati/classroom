from functools import reduce
def even_sum():
	total=0
	mylist=[]
	for i in range(0,10):
		if(i%2==0):
			#print(i)
			mylist.append(i**2)
	print(mylist)

	total = total + reduce((lambda x,y: x + y),mylist)
	print(total)
even_sum()

