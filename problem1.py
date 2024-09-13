#Given K sorted arrays of size N each, the task is to merge them all maintaining their sorted order.
num_arrays = int(input("Enter number of arrays (K) = "))
num_elements = int(input("Enter number of elements in each array (N) = "))  # N is unused in logic
input_arrays = [] 
combined_array = [] 
def insertion_sort(arr): 
    for i in range(1, len(arr)):  
        current_element = arr[i] 
        j = i - 1 
        while j >= 0:
            if arr[j] > current_element:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = current_element
    return arr

for _ in range(num_arrays):  
    user_input = list(map(int, input("Enter sorted array: ").split()))
    input_arrays.append(user_input)

for array in input_arrays:  
    combined_array.extend(array)

print("Merged array in a sorted order:", insertion_sort(combined_array))
