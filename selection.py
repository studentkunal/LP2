# Selection Sort using Greedy Approach

def selection_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        min_index = i  # Assume current index is minimum

        # Find the minimum element in remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Taking user input
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

# Call function
sorted_arr = selection_sort(arr)

# Output
print("Sorted array:", sorted_arr)