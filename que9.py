#Write a Python function that takes two sorted arrays and merges them into a single sorted array.

def merge_sorted_arrays(arr1,arr2):
    i,j = 0 ,0
    merged = []

    while  i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    return merged

arr1 = [1,3,4,6]
arr2 = [2,5,4,7]
merged_array = merge_sorted_arrays(arr1 , arr2)
print(merged_array) 