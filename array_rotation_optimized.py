
""" This is left rotation """
def arr_rotate(arr, k):
    for j in range(k):
        arr.append(arr[j])
    arr = arr[k:]
    return arr
nums1 = [3, 4, 2, 6, 8, 10]
nums2 = [13, 24, 42, 67, 80, 1]

print(arr_rotate(nums1,2))
print(arr_rotate(nums2,4))


#Optimum solution with O(n) time complexity

""" This is right rotation """

def arr_reverse(arr, i, j):
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr


def arr_right_rotate_using_swap(arr, k):
    
    k = k%len(arr)
    
    """Swap the second half of the array"""
    arr_reverse(arr, len(arr)-k, len(arr)-1)
    """Swap the first half of the array"""
    arr_reverse(arr, 0, len(arr)-k-1)
    """reverse the entire obtained array"""
    arr_reverse(arr, 0, len(arr)-1)
    return arr

nums1 = [3, 4, 2, 6, 8, 10]
nums2 = [13, 24, 42, 67, 80, 1]
nums3 = [1, 2, 3, 4, 5]

print(arr_right_rotate_using_swap(nums1,2))
print(arr_right_rotate_using_swap(nums2,4))
print(arr_right_rotate_using_swap(nums3,2))



def arr_left_rotate_using_swap(arr, k):
    
    k = k%len(arr)
    
    """Swap the second half of the array"""
    arr_reverse(arr, k, len(arr)-1)
    """Swap the first half of the array"""
    arr_reverse(arr, 0, k-1)
    """reverse the entire obtained array"""
    arr_reverse(arr, 0, len(arr)-1)
    return arr

nums1 = [3, 4, 2, 6, 8, 10]
nums2 = [13, 24, 42, 67, 80, 1]
nums3 = [1, 2, 3, 4, 5]

print(arr_left_rotate_using_swap(nums1,2))
print(arr_left_rotate_using_swap(nums2,4))
print(arr_left_rotate_using_swap(nums3,2))
