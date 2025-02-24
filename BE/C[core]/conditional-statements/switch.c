#include<stdio.h>

int main(){
    // 0 - mon
    // 6 - sun

    int day = 4;
    switch(day + 3){
    case 0:
        printf("Today is mon.");
        break;
    case 1:
        printf("Today is tue.");
        break;
    case 2:
        printf("Today is wed.");
        break;
    case 3:
        printf("Today is thu.");
        break;
    case 4:
        printf("Today is fri.");
        break;
    case 5:
        printf("Today is sat.");
        break;
    case 6:
        printf("Today is sun.");
        break;
    default:
        printf("Invalid day.\nPlease enter a valid day.");
    }
}
