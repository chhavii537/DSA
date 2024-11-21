#Write a Python program that removes all duplicate elements from an array without using any built-in set operations.
def remove_duplicate(arr):
    unique = []
    for element in arr:
        if element not in unique:
            unique.append(element)
    return unique

arr = [1,2,2,3,4,4,5,6]
arr1 = remove_duplicate(arr)
print(arr1)

    