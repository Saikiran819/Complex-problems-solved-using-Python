

def select_sort(arr):
    k = 0
    while k < len(arr)-1:
        print(arr)
        currmin = arr[k]
        i = k + 1
        while i < len(arr):
            if currmin > arr[i]:
                currmin = arr[i]
                foundnewcurr = True
                j = i
            i += 1
        if foundnewcurr == True:
            arr[k], arr[j] = arr[j], arr[k]
            foundnewcurr = False
            
        k += 1

arr = [12, 25, 0, 16, 54, 36, 75, 21, 45, 15, 37, 49, 64, 77, 98, 12]

select_sort(arr)
print(arr)