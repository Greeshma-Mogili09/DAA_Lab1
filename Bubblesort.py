import time
import random

def bubble_sort(A):
    swap_count = 0  
    comparison_count = 0  
    pass_count = 0  
    
    for i in range(0, len(A)):    
        pass_count += 1  
        for j in range(i+1, len(A)):    
            comparison_count += 1  
            if A[j] < A[i]:    
                temp = A[j]    
                A[j] = A[i]    
                A[i] = temp    
                swap_count += 1  

    return swap_count, comparison_count, pass_count

n = int(input("Enter number of elements in the array: "))
A = [random.randint(1, 100) for _ in range(n)]

print("Before sorting array elements are - ") 
for i in A:    
    print(i, end=" ")   

start_time = time.time()  # Start measuring time

swap_count, comparison_count, pass_count = bubble_sort(A)

end_time = time.time()  # End measuring time

# Sort the array
A.sort()

print("\nAfter sorting array elements are - ")   
for i in A:    
    print(i, end=" ")   

print("\nNumber of passes:", pass_count)
print("Number of swaps:", swap_count)
print("Number of comparisons:", comparison_count)

time_taken = (end_time - start_time) * 1000
print("Execution Time of the bubble sort algorithm is : {:.3f} milliseconds".format(time_taken))
