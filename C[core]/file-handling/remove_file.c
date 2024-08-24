#include<stdio.h>

void main(){
 char file_name[100] = "sample.txt";
 int res = remove(file_name);

 if(res == 0){
    printf("File is deleted.");
 }
}
