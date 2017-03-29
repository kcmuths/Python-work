##Program to perform binary search and determine the number of calls that 
##are made when the length of the list is specified

def bSearch(L, e, low, high):
    global numCalls
    numCalls += 1
    if high - low < 2:
	return L[low] == e or L[high] == e
    mid = low + int((high - low) / 2)
    if L[mid] == e:
        return True
    if L[mid] > e:
        return bSearch(L, e, low, mid - 1)
    else:
        return bSearch(L, e, mid + 1, high)

def search(L, e):
    return bSearch(L, e, 0, len(L) - 1)

L = range(100)
numCalls = 0
search(L, 100)
msg = 'Number of calls when length = '
print msg + str(len(L)) + ' is', numCalls
L = range(200)
numCalls = 0
search(L, 200)
print msg + str(len(L)) + ' is', numCalls
L = range(400)
numCalls = 0
search(L, 400)
print msg + str(len(L)) + ' is',numCalls

          
