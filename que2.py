#Reverse an Array
def reverse_array(arr):
    #given 2 pointers
    start = 0
    end = len(arr) -1
    # Swap elements while moving pointers towards the center
    while start < end:
        # Swap elements at the start and end
        arr[start] ,arr[end] = arr[end] , arr[start]
        #move the pointers
        start += 1
        end -= 1
arr = [1,2,3,4,5]
reverse_array(arr)
print(arr)

