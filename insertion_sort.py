
def insertion_sort(arr):
    
    for i in range(1, len(arr)):
        key = arr[i]
        
        prev_idx = i - 1
        while prev_idx >= 0 and key < arr[prev_idx]:
            print("key = ", key, end = "\n")
            print("prev_idx = ", prev_idx, end = "\n")
            print("i = ", i, end = "\n")
            print(arr)
            arr[prev_idx+1] = arr[prev_idx]
            prev_idx -= 1
        arr[prev_idx+1] = key
        print(arr)
arr = [12, 25, 0, 16, 54, 36, 75, 21, 45, 15, 37, 49, 64, 77, 98, 12]    
insertion_sort(arr)
print(arr)