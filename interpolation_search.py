

nums1 = [10, 5, 8, 67, 32, 11, 12, 17, 3]
nums2 = [1, 25, 81, 7, 2, 21, 18, 17, 36]
nums3 = [0, 50, 68, 6, 3, 15, 52, 7, 43]

def interpolation_search(nums, key, low, high):
    nums.sort()
    print(nums)
    
    mid = low + int(((float(high - low) / (nums[high] - nums[low]) * (key - nums[low]))))
    
    key_found = False
    
    while low <= high and key >= nums[low] and key <= nums[high]:
        if key == nums[mid]:
            key_found = True
            break
        elif key < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
        mid = low + int(((float(high - low) / (nums[high] - nums[low]) * (key - nums[low]))))
        
    if not key_found:
        print("Key = {0} not found".format(key))
    else:
        print("{0} is found at index {1}".format(key, mid))

interpolation_search(nums1, 10, 0, 8)
interpolation_search(nums2, 81, 0, 8)
interpolation_search(nums3, 1, 0, 8)