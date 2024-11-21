#Write a Python function to rotate an array by K positions to the right.
def reverse(arr,start,end):
    while start < end:
        arr[start] , arr[end] = arr[end] , arr[start]
        start += 1
        end -= 1

def right_rotate(arr , k):
    n = len(arr)
    k = k % n

    # Step 1: Reverse the entire array
    reverse(arr , 0 ,n-1)
    # Step 2: Reverse the first K elements
    reverse(arr , 0 , k-1)
    # Step 3: Reverse the remaining n - K elements
    reverse(arr, k, n-1)

    return arr

arr = [1,2,3,4,5,6,7]
k = 3
print(arr)
rotated_array = right_rotate(arr , k)
print(rotated_array)
