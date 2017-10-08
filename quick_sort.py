import copy
import time

def quick_partition(array, i, j):
	swap = array[i]
	while j > i:
		print array[j]
		while j > i and array[j] >= swap:
			j = j - 1
		if j > i:
			array[i] = array[j]
			i = i + 1
		while j > i and array[i] <= swap:
			i = i + 1
		if j > i:
			array[j] = array[i]
			j = j - 1
	array[i] = swap
	return i


def quick_sort(array, s, t):	
	if(s < t):
		i = quick_partition(array, s, t)
		quick_sort(array, s, i-1)
		quick_sort(array, i+1, t)