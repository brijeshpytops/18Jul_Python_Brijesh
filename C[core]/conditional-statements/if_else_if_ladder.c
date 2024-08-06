#include<stdio.h>

int main(){
    float score = 500;

    if (score <= 100 && score >= 0){
        if (score >= 80){
        printf("Class A");
    }else if(score >= 60){
        printf("Class B");
    }else if(score >= 40){
        printf("Class C");
    }else{
        printf("You are failed.");
    }
    }else{
        printf("Invalid score.\nPlease enter a valid score.");
    }


}
