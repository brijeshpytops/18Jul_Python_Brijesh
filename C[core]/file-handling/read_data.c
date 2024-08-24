#include<stdio.h>

void main(){
    FILE *f;
    char data[100];

    f = fopen("sample.txt", "r");


    // read data from the file.
    fgets(data, sizeof(data), f);

    printf("Data: %s", data);
    fclose(f);

}

