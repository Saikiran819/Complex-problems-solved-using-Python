

arr = [1, 25, 0, 74, 26, 42, 32, 37, 12, 5, 7, 50]
n = int(input("Enter a integer value:\n"))
arr.sort()
found = False
for i in range(len(arr)-2):
    l = i + 1
    r = len(arr)-1
    while l < r:
        if arr[i] + arr[l] + arr[r] == n:
            print("The triplet is: {0}, {1}, {2}".format(arr[i], arr[l], arr[r]))
            found = True
            break
        elif arr[i] + arr[l] + arr[r] < n:
            l += 1
        else:
            r-=1
if not found:
    print("Triplet sum not found\n")