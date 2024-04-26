def linear_search(arr, target):
    """
    Returns:
    - index: The index of the target element if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target element if found
    return -1  # Return -1 if target element is not found

# Example usage:
arr = [4, 2, 7, 1, 9, 5]
target = -7
index = linear_search(arr, target)
if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the array.")