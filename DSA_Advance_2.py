# 1. Implement Binary Search

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid

    return -1

arr = input("Enter the array (space-separated): ").split()
arr = [int(i) for i in arr]

x = int(input("Enter the element to search for: "))

result = binary_search(arr, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")


# 2. Implement Merge Sort

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr

arr = input("Enter the array to be sorted: ").split()
arr = [int(i) for i in arr]

sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)

# 3. Implement Quick Sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quick_sort(left) + [pivot] + quick_sort(right)

arr = input("Enter the array (space-separated): ").split()
arr = [int(i) for i in arr]

sorted_arr = quick_sort(arr)

print("Sorted array:", sorted_arr)

# 4. Implement Insertion Sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = input("Enter the array (space-separated): ").split()
arr = [int(i) for i in arr]

sorted_arr = insertion_sort(arr)

print("Sorted array:", sorted_arr)

# 5. Write a program to sort list of strings (similar to that of dictionary)

def sort_dict_strings(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = input("Enter the list of strings (comma-separated): ").split(",")
arr = [i.strip() for i in arr]

sorted_arr = sort_dict_strings(arr)

print("Sorted list:", sorted_arr)