#Sum of Elements in an Array
def sum_of_elements(arr):
    total = 0
    for num in arr:
        total += num
    return total
arr = [12,24,89,4,4]
result = sum_of_elements(arr)
print(result) 
    