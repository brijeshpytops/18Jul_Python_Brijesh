// What is function in c?
// In C programming, a function is a block of code designed to perform a specific task. Functions help to modularize and organize code, allowing you to break down complex programs into smaller, manageable sections.

syntax:

// Function declaration
// return_type function_name(parameter_list) {
//     // Function body
//     return return_value;
// }

// Function call
// function_name(argument_values);

Example :

#include <stdio.h>

int add(int a, int b){
  return a + b;
}

int main()
{
    printf("total = %d\n",add(10, 20));
    printf("total = %d\n",add(30, 40));
    printf("total = %d\n",add(50, 60));
    return 0;
}

In the provided example, the add() function takes two integer arguments and returns their sum. The main() function calls the add() function multiple times with different argument values and prints the results. The return statement in the main() function is used to indicate that the program should terminate.

There are two types of function in c:

1. User-defined functions: These are functions that are defined by the user and can be called from anywhere in the program. They can accept arguments and return values.

2. Library(Built-in) functions: These are predefined functions that are available in the C library and can be used directly in the program without defining them. Examples include printf(), scanf(), and exit().

In summary, functions in C are blocks of code designed to perform specific tasks. They help to modularize and organize code, making it easier to read, understand, and maintain. User-defined functions allow you to reuse code and write cleaner, more maintainable programs. Library functions provide built-in functionality that can be used directly in your program without writing custom code.

Note: This is a simplified explanation of functions in C. For a more detailed and in-depth understanding, you can refer to the official C programming language documentation or online resources.

user-define function ways to define:
1] with return_type with parameter_list
Example:
    #include <stdio.h>

    int add(int a, int b){
    return a + b;
    }

    int main()
    {
        printf("total = %d\n",add(10, 20));
        printf("total = %d\n",add(30, 40));
        printf("total = %d\n",add(50, 60));
        return 0;
    }
2] without return_type with parameter_list
Example: 
    #include <stdio.h>

    void add(int a, int b){
        printf("Total : %d\n",a + b);
    }

    int main()
    {
        add(10, 20);
        add(30, 40);
        add(50, 60);
        return 0;
    }

3] with return_type without parameter_list  
Example: 
    #include <stdio.h>

    int add(){
        int a = 10, b = 20;
        return a + b;
    }

    int main()
    {
        printf("Total : %d\n",add());
        printf("Total : %d\n",add());
        printf("Total : %d\n",add());
        return 0;
    }
4] without return_type and without parameter_list
Example:
    #include <stdio.h>

    void add(){
        int a = 10, b = 20;
        printf("Total : %d\n",a + b);
    }

    int main()
    {
        add();
        add();
        add();
        return 0;
    }



Recursive functions :

Recursive functions in C are functions that call themselves in order to solve a problem. Recursion is a powerful programming technique where a function solves a problem by breaking it down into smaller, more manageable subproblems of the same type.

Syntax:

// Recursive function declaration

return_type function_name(parameter_list) {
    // Base case
    if (condition) {
        return base_value;
    }

    // Recursive case
    return function_name(modified_parameter_list);
}

Example:
1 * 2 * 3 * 4 *... * n

#include <stdio.h>

int factorial(int num){
    if (num == 1){
      return 1;
    }else{
      return num * factorial(num - 1);
    }
}

int main()
{
    printf("Total : %d\n",factorial(5));
    return 0;
}

(1 + 2) + (2 +  3) + ... + (n + (n+1))
(5 + 6) + (4 + 5) + (3 + 4) + (2 + 3) + (1 + 2)
#include <stdio.h>

int num_inc(int num){
    if (num == 1){
      return  (num + (num + 1));
    }else{
      return (num + (num + 1)) + num_inc(num - 1);
    }
}

int main()
{
    printf("Total : %d\n",num_inc(5));
    return 0;
}

0 1 1 2 3 5 8 13 ....

#include <stdio.h>

int fibonacci(int num){
    if (num <= 1){
      return num;
    } else{
      return fibonacci(num - 1) + fibonacci(num - 2);
    }
}

int main()
 {
    printf("Total : %d\n",fibonacci(10));
    return 0;
}
