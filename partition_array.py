def partition_array(numbers):
    pivot = numbers[-1] #assign last element as reference element
    i = 0  #to access each element of the list
    j = 0  #to know/find the index of the pivot element 

    for i in range(len(numbers)-1):
        if numbers[i] < pivot:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            j += 1
    numbers[-1], numbers[j] = numbers[j], numbers[-1]

