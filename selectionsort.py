import time
import random

def selection_sort(A):
    swap_count = 0  
    comparison_count = 0  
    pass_count = 0  
    
    for i in range(len(A)):    
        pass_count += 1
        min_index = i
        for j in range(i+1, len(A)):    
            comparison_count += 1
            if A[j] < A[min_index]:    
                min_index = j    
        if min_index != i:
            A[i], A[min_index] = A[min_index], A[i]
            swap_count += 1  

    return swap_count, comparison_count, pass_count

n = int(input("Enter number of elements in the array: "))
A = [random.randint(1, 100) for _ in range(n)]

print("Before sorting array elements are - ") 
for i in A:    
    print(i, end=" ")   

start_time = time.time()  
swap_count, comparison_count, pass_count = selection_sort(A)
end_time = time.time()

# Sort the array
A.sort()

print("\nAfter sorting array elements are - ")   
for i in A:    
    print(i, end=" ")   

print("\nNumber of passes:", pass_count)
print("Number of swaps:", swap_count)
print("Number of comparisons:", comparison_count)

time_taken = (end_time - start_time) * 1000
print("Execution Time of the selection sort algorithm is - {:.3f} milliseconds".format(time_taken))
