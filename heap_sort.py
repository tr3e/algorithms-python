import time
def sift(array, s, t):
    parent = s
    child = s * 2
    key = array[s]
    finished = False
    while child <= t and (not finished):
        if child < t and array[child] < array[child + 1]:
            child = child + 1
        if array[child] < key:
            finished = True
        else:
            array[parent] = array[child]
            parent = child
            child = child * 2
    array[parent] = key

def heap_sort(array, n):
    #n is length-1 cause without array[0]
    start = time.time()
    for i in reversed(xrange(1, n / 2 + 1)):
        sift(array, i, n)
    #print array
    for i in reversed(xrange(2, n + 1)):
        temp = array[1]
        array[1] = array[i]
        array[i] = temp
        #print array
        sift(array, 1, i - 1)
        #print array[:i]
    end = time.time()
    print end - start
