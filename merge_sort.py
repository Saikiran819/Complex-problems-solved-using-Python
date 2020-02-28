def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums)//2
        lhalf = nums[:mid]
        rhalf = nums[mid:]
        print(lhalf)
        print(rhalf)
        merge_sort(lhalf)
        merge_sort(rhalf)
        i = j = k = 0
        while i < len(lhalf) and j < len(rhalf):
            print("nums = ", nums)
            if lhalf[i] < rhalf[j]:
                nums[k] = lhalf[i]
                i += 1
            else:
                nums[k] = rhalf[j]
                j += 1
            k = k + 1
        while i < len(lhalf):
            nums[k] = lhalf[i]
            i += 1
            k += 1
        while j < len(rhalf):
            nums[k] = rhalf[j]
            j += 1
            k += 1

arr = [12, 25, 0, 16, 54, 36, 75, 21, 45, 15, 37, 49]
merge_sort(arr)
print(arr)