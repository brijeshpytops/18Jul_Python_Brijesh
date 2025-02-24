// Conditional Operators
#include <stdio.h>

int main() {
    int bal = 1000, wb=5000;

    // syntax : (condition)?True:False;

    (wb <= bal)?printf("withdrow successful."):printf("insufficent balance");
    return 0;
}