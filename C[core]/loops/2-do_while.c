#include <stdio.h>

int main() {
    // finite loop
    int start = 1;
    int end = 10;
    int table = 2256456;
    do{
        printf("%d * %d = %d\n", table, start, start*table);
        start++;
    }while (start <= end);

    return 0;
}