"""
Bubble Sort Algorithm
No of elements: n
No of passes: n - 1
No of comparision: 1+2+3+...+n = (n(n-1))/2 = O(n^2)
No of comparision: 1+2+3+...+n = (n(n-1))/2 = O(n^2)

Time Complexity:
Minimum : O(n)
Maximum: O(n^2)

Bubble Sort algorithm is Adaptive, Stable
"""

def bubbleSort(arr):
	for i in range(len(arr) - 1):

		# If the list is already sorted then, flag will remain zero. 
		# No need to iterate again. Time complexity will be O(n)
		flag = 0 
		for j in range(len(arr) - 1 - i):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				flag = 1
		if flag == 0: #If flag is zero, means list is sorted
			break
	return arr

unsorted_list = [1,5,3,7,4,98,25,75,34,6,19,55,22,88,46]
print('Before Sorting: ', unsorted_list)
sorted_list = bubbleSort(unsorted_list)
print('After Sorting: ', sorted_list)



