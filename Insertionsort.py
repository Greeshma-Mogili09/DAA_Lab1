import time
import random

def insertion_sort(A):
    swap_count = 0  
    comparison_count = 0  
    pass_count = 0  
    
    for i in range(1, len(A)):
        pass_count += 1
        key = A[i]
        j = i - 1
        while j >= 0 and key < A[j]:
            comparison_count += 1
            A[j + 1] = A[j]
            j -= 1
            swap_count += 1
        A[j + 1] = key

    return swap_count, comparison_count, pass_count

n = int(input("Enter number of elements in the array: "))
A = [random.randint(1, 100) for _ in range(n)]

print("Before sorting array elements are - ") 
for i in A:    
    print(i, end=" ")   

start_time = time.time()  
swap_count, comparison_count, pass_count = insertion_sort(A)
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
print("Execution Time of the insertion sort algorithm is - {:.3f} milliseconds".format(time_taken))
