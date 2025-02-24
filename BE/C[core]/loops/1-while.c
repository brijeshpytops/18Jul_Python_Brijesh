// Example -1:
#include <stdio.h>

int main() {
    // infinite loop
    while (1){
        printf("Tops");
    }

    return 0;
}

// Example -2:

#include <stdio.h>

int main() {
    // infinite loop
    while (1){
        int age;
    float weight;

    printf("Enter your age:");
    scanf("%d", &age);

    if(age >= 18){
        printf("Enter your weight:");
        scanf("%f", &weight);
        if(weight >= 50){
            printf("You can donate.\n\n");
        }else{
            printf("You can not donate because of your weight is lessthen 50\n\n");
        }
    }else{
        printf("You can not donate because of your age is lessthen 18\n\n");
    }
    }

    return 0;
}

// Example : 3

#include <stdio.h>

int main() {
    // finite loop
    int start = 1;
    int end = 10;
    int table = 2256456;
    while (start <= end){
        printf("%d * %d = %d\n", table, start, start*table);
        start++;
    }

    return 0;
}