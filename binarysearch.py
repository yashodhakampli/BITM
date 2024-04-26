def binary_search(arr, target):
    """
    Perform binary search on the given sorted array to find the target element.
    
    Args:
    - arr: The sorted array to search in.
    - target: The element to search for.
    
    Returns:
    - index: The index of the target element if found, otherwise -1.
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    
    # If target is not present in the array
    return -1

# Example usage:
#arr = [1, 3, 5, 7, 9, 11, 13]
arr = ['apple','banana','carrot','chennai','zebra']
target = 'chennai'
index = binary_search(arr, target)
if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the array.")