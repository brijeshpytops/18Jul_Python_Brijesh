// What is an array?
// An array in C is a collection of elements of the same data type stored in contiguous memory locations. Arrays are used to store multiple values in a single variable, instead of declaring separate variables for each value.

// Key Points about Arrays in C:
// Data Type Consistency: All elements of the array must be of the same data type (e.g., int, char, float).

// Fixed Size: The size of the array is fixed at the time of declaration, meaning the number of elements it can hold is predefined and cannot be changed during runtime.

// Zero-Based Indexing: Array elements are accessed using an index, which starts from 0. The first element is at index 0, the second at index 1, and so on.

// Contiguous Memory Allocation: All elements of the array are stored in contiguous memory locations. This allows efficient access to array elements using the index.


// one-dim array:

// syntax:

// data_type array_name[size] = {val1, val2,....valn};

// int stu1 = 56;
// printf("%d", stu1);


#include <stdio.h>
int main()
{
    float students[] = {
      56.0, 78.0, 98.0, 80.0, 69.0, 87.0
    };
    // access specific element from the arrya
    // printf("%.2f", students[0]);
    // 56.0 - 4 bytes * 5 = 20/4 = 5
    
    int len = sizeof(students)/sizeof(students[0]);
    // printf("Length of array is : %d", len);
    
    for( int start = 1; start <= len; start++){
      int index = start-1;
      printf("%.2f\n", students[index]);
    }
}