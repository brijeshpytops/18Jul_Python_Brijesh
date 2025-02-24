// syntax:

// data_type array_name[row][col] = {
//     {value1, value2,..., valueN},
//     //...
//     {value1, value2,..., valueN}
// }

// 1 2 3
// 4 5 6

// 11 22 33 
// 44 55 66
// 77 88 99

// Example-1:

#include <stdio.h>
int main()
{
   int matrix1[2][3] = {
     {1,2,3},
     {4,5,6}
   };
   int matrix2[2][3] = {
     {11,22,33},
     {44,55,66}
   };
   
   // using single element from muli-dim array
  // printf("%d", matrix1[0][2]);
   
   
  int len_row = sizeof(matrix1)/sizeof(matrix1[0]);
  int len_col = sizeof(matrix1[0])/sizeof(matrix1[0][0]);
   
  // printf("Row: %d, Col:  %d", len_row, len_col);
  
  printf("Matrix-1: \n");
  for(int row = 0; row < len_row; row++){
    for(int col = 0; col < len_col; col++){
      printf("%d ", matrix1[row][col]);
    }
    printf("\n");
  }
  printf("Matrix-2: \n");
  for(int row = 0; row < len_row; row++){
    for(int col = 0; col < len_col; col++){
      printf("%d ", matrix2[row][col]);
    }
    printf("\n");
  }
  printf("Matrix-1 + Matrix-2: \n");
  for(int row = 0; row < len_row; row++){
    for(int col = 0; col < len_col; col++){
      printf("%d ", matrix1[row][col] + matrix2[row][col]);
    }
    printf("\n");
  }
}

// Example -2 :

#include <stdio.h>
int main()
{
   int matrix1[2][3] = {
     {1,2,3},
     {4,5,6}
   };
   int matrix2[2][3] = {
     {11,22,33},
     {44,55,66}
   };
   
   // using single element from muli-dim array
  // printf("%d", matrix1[0][2]);
   
   
  int len_row = sizeof(matrix1)/sizeof(matrix1[0]);
  int len_col = sizeof(matrix1[0])/sizeof(matrix1[0][0]);
   
  // printf("Row: %d, Col:  %d", len_row, len_col);
  
  printf("Matrix-1: \n");
  for(int row = 0; row < len_row; row++){
    for(int col = 0; col < len_col; col++){
      printf("%d ", matrix1[row][col]);
    }
    printf("\n");
  }
  printf("Matrix-2: \n");
  for(int row = 0; row < len_row; row++){
    for(int col = 0; col < len_col; col++){
      printf("%d ", matrix2[row][col]);
    }
    printf("\n");
  }
  printf("Matrix-1 * Matrix-2: \n");
  for(int row = 0; row < len_row; row++){
    for(int col = 0; col < len_col; col++){
      printf("%d ", matrix1[row][col] * matrix2[row][col]);
    }
    printf("\n");
  }
}