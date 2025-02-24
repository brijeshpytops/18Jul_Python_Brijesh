// Relational Operators
#include <stdio.h>

int main() {
    int num1 = 10, num2 = 20, num3 = 10, res;
    // 0 - false, 1 - true
    
    res = num1 == num2;
    res = num1 != num2;
    res = num1 == num3;
    res = num1 < num2;
    res = num1 <= num2;
    res = num1 > num2;
    res = num1 >= num2;
 
    printf("Res = %d", res);
    
    

    return 0;
}