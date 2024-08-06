
#include<stdio.h>

int main(){
    float bal = 10000;
    float wb = 15000;

    if (wb <= bal){
        printf("Withdrow done.\nYour remaingin amount is %f", bal-wb);

    }else{
        printf("Inssufficent amount.");
    }
}
