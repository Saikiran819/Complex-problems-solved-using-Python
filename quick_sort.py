

def partition(arr, first, last):
    
    pivot = arr[first]
    
    left = first + 1
    right = last
    done = False
    
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while right >= left and arr[right] >= pivot:
            right -=1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
            
    arr[first], arr[right] = arr[right], arr[first]
    return right

def quick_sort(arr, first, last):
    if first < last:
        split = partition(arr, first, last)
        quick_sort(arr, first, split-1)
        quick_sort(arr, split+1, last)

arr = [12, 25, 0, 16, 54, 36, 75, 21, 45]
quick_sort(arr, 0, len(arr)-1)
print(arr)