

def LIS (arr):
    lis = []
    lis = [1]*len(arr)
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                
    return lis
    
nums1 = [1, 9, 3, 10, 4, 20, 2]
nums2 = [50, 3, 10, 7, 40, 80]
nums3 = [3, 10, 2, 1, 20]
nums4 = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

print(max(LIS(nums1)))
print(max(LIS(nums2)))
print(max(LIS(nums3)))
print(max(LIS(nums4)))


def lisarray(arr):
    maxi = 0
    k = 1
    lis = LIS(arr)
    lisarr = []
    m = max(lis)
    
    #while len(lisarr) < m:
     #   print(lis)
    for i in range(len(lis)):
        if lis[i] > maxi:
            if len(lisarr) > 0:
                if lisarr[-1] <= arr[i]:
                    lisarr.append(arr[i])
                    maxi = lis[i]
            else:
                lisarr.append(arr[i])
                maxi = lis[i]
    """
      if len(lisarr) < m:
            while len(lisarr):
                lisarr.pop()
            if k < len(lis) - 2:
                lis = lis[k:]
                k += 1
        elif len(lisarr) == m:
            break
    """
    print(lisarr)

lisarray(nums1)
lisarray(nums2)
lisarray(nums3)
lisarray(nums4)