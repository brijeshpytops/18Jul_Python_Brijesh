// documentation section
// write a prgram and print the n number of fiboonaci series

// linking section
#include <stdio.h>
#include <ctime.h>
#include <string.h>  

// global declaration section
float PI = 3.14;

// function declaration section

// main function declaration section
int main(){
    // set of instruction [block of code]
    int n, i, a = 0, b = 1;
    printf("Enter the number of terms: ");
    scanf("%d", &n);

    printf("Fibonacci Series: \n");
    for (i = 0; i < n; i++) {
        printf("%d ", a);
        int temp = a + b;
        a = b;
        b = temp;
    }
    return 0; // return 0 to indicate successful termination of the program

    // end of the main function


}

// sub function declaration section