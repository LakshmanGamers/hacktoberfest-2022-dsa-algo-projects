def bubbleSort(array):
    n = len(arr)
    #if the array is already sorted (no swapping has occured) , so that we can stop the process
    swapped = False
    #traverse through all elements in array
    for i in range(n-1):
        for j in range(0, n-i-1):
            # traverse elements from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if array[j] > array[j + 1]:
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]
         
        if not swapped:
            #if single swap also didnt occured then it represents array is already sorted , hence we exit from loop
            return

 
array=[8,9,1232,1,22,32,43]
print("Unsorted Array is :")
print(array)
bubbleSort(array)
print("Array After Applying Bubble Sort")
print(array)

