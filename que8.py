#Given an array of size n-1 with elements from 1 to n (one number is missing), write a function to find the missing number

def find_missing_number(arr,n):
    # Calculate the expected sum of numbers from 1 to n
    expected_sum = n * (n+1) // 2
    # Calculate the actual sum of the given arra
    actual_sum = sum(arr)
    missing_number = expected_sum - actual_sum
    return missing_number
arr = [1,2,4,5,6,7]
n = 7
missing = find_missing_number(arr, n)
print(missing)


 