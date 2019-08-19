
def bubble_sort(llist):
	"""
	In bubble sort it changes the original list.
	"""
	length = len(llist)
	for i in range(length):
		for j in range(length - i - 1):
			if llist[j] > llist[j+1]:
				llist[j],llist[j+1] = llist[j+1],llist[j]
	return llist

llist = [1,2,5,7,9,13,29,64,35,87,56,8,47,86,54]
print(llist) #Before sorting
bubble_sort(llist)
print(llist) #After sorting

