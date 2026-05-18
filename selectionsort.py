def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i

        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index=j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    
    return arr

print("Selection Sort: ")
print(selection_sort([65,21,32,11,1,67]))