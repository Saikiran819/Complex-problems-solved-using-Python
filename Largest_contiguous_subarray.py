


def largest_cnt_subarray(arr):
    
    result = 0
    tot_sum = 0
    beg = 0
    end = 0
    sub = []
    maxlen = 0
    
    for i in range(len(arr)):
        
        tot_sum += arr[i]
        if tot_sum < 0:
            tot_sum = 0
            beg = i+1
        if result < tot_sum:
            result = tot_sum
            end = i
            maxlen = end - beg + 1
            sub = arr[beg:end + 1]
        elif result == tot_sum:
            newend = i
            if newend - beg + 1 > maxlen:
                maxlen = newend - beg + 1
                sub = arr[beg:newend + 1]
            end = newend
    print("beg index = ", beg)
    print("end index = ", end)
    print("Max Sub array = ", sub)
    return result

nums1 = [-2, -3, 4, -1, -2, 1, 5, -3]
nums2 = [5, -2, -1, 3, -4]
nums3 = [-2, -3, 4, -1, -2, 1, 5, -3]
nums4 = [6, -4, -2, 5, 1, -6, 2, 4]


print("MAX CONT SUM = ", largest_cnt_subarray(nums1))
print("MAX CONT SUM = ", largest_cnt_subarray(nums2))
print("MAX CONT SUM = ", largest_cnt_subarray(nums3))
print("MAX CONT SUM = ", largest_cnt_subarray(nums4))
