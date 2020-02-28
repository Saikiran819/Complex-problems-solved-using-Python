
def shell_sort(arr):
    
    gap = len(arr)//2
    
    while gap > 0:
        for i in range(gap, len(arr)):
            key = arr[i]
            j = i
            while j >= gap and key < arr[j-gap]:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = key
        gap //= 2
arr = [12, 25, 0, 16, 54, 36, 75, 21, 45, 15, 37, 49, 64, 77, 98, 12]    
shell_sort(arr)
print(arr)