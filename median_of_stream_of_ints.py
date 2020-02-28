minheap = []
maxheap = []
minlen = 0
maxlen = 0
listofnums = [1, 2, 4, 10, 11, 29, 36, 78, 45, 23]

def push(heap, n):
    global minlen
    global maxlen
    
    if heap == minheap:
        minheap.append(n)
        minlen+=1
        i = minlen-1
        while (i-1)//2 >= 0 and minheap[i] < minheap[(i-1)//2]:        
            minheap[i], minheap[(i-1)//2] = minheap[(i-1)//2], minheap[i]
            i = (i-1)//2
    elif heap == maxheap:
         maxheap.append(n)
         maxlen+=1
         i = maxlen-1
         while (i-1)//2 >= 0 and maxheap[i] > maxheap[(i-1)//2]:
            maxheap[i], maxheap[(i-1)//2] = maxheap[(i-1)//2], maxheap[i]
            i = (i-1)//2


def rem(heap, n):
    global minlen
    global maxlen
    
    if heap == minheap:
        minheap[0] = minheap[minlen-1]
        del(minheap[minlen-1])
        minlen-=1
        if minlen == 2 and minheap[0] > minheap[1]:
            minheap[0], minheap[1] = minheap[1], minheap[0]
        else:
            i = 0
            while 2*i+2 < minlen and (minheap[i] > minheap[(2*i+1)] or minheap[i] > minheap[(2*i+2)]):
                if minheap[(2*i+1)] < minheap[(2*i+2)]:
                    minheap[i], minheap[(2*i+1)] = minheap[(2*i+1)], minheap[i]
                    i = 2*i+1
                else:
                    minheap[i], minheap[(2*i+2)] = minheap[(2*i+2)], minheap[i]
                    i = 2*i+2
    elif heap == maxheap:
        maxheap[0] = maxheap[minlen-1]
        del(maxheap[maxlen-1])
        maxlen-=1
        i = 0
        while 2*i+2 < maxlen and (maxheap[i] < maxheap[(2*i+1)] or maxheap[i] < maxheap[(2*i+2)]):
            if maxheap[(2*i+1)] > maxheap[(2*i+2)]:
                maxheap[i], maxheap[(2*i+1)] = maxheap[(2*i+1)], maxheap[i]
                i = 2*i+1
            else:
                maxheap[i], maxheap[(2*i+2)] = maxheap[(2*i+2)], maxheap[i]
                i = 2*i+2


def median_of_stream(nums):
    global maxlen
    global minlen
    maxheap.append(nums[0])
    maxlen = 1
    print("median = ", maxheap[0])
    for v in nums[1:]:
            if v>maxheap[0]:
                push(minheap, v)
            else:
                push(maxheap, v)
        
            if len(minheap) == len(maxheap) + 2:
                push(maxheap, minheap[0])
                rem(minheap, v)
            elif len(maxheap) == len(minheap) + 2:
                push(minheap, maxheap[0])
                rem(maxheap, v)
            
            if len(minheap) == len(maxheap):
                print("median = ",(maxheap[0] + minheap[0])/2)
            elif len(minheap) == len(maxheap) + 1:
                print("median = ",minheap[0])
            elif len(maxheap) == len(minheap) + 1:
                print("median = ",maxheap[0])
                
median_of_stream(listofnums)