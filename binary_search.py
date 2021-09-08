
def binarySearch(arr,x):
    l=0
    r=len(arr)

    while l<=r:
        mid = (l + r )// 2
        if arr[mid] == x:   # Check if x is present at mid
            return mid+1
        elif arr[mid] < x:  # If x is greater, ignore left half
            l = mid + 1
        else:               # If x is smaller, ignore right half
            r = mid - 1

    return -1

arr=[ 2, 3, 4, 10, 40,56,112,140]
x = int(input("enter a numb u wanna search: "))

result = binarySearch(arr, x)

if result != -1:
	print (f"Element is present at index {result} ")
else:
	print ("Element is not present in array")
