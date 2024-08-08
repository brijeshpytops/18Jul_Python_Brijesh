#include <stdio.h>

int main() {
    int table = 10;
    for(int start = 1; start<=10; start++){
        printf("%d * %d = %d\n", table, start, start*table);
    }
    return 0;
}

#include <stdio.h>

int main() {
    int table = 10;
    for(int start = 10; start>=1; start--){
        printf("%d * %d = %d\n", table, start, start*table);
    }

    return 0;
}