#include<stdio.h>

void main(){
    FILE *f;
    char data[100];

    f = fopen("sample.txt", "w");

    if (f == NULL) {
        perror("Error opening file");
    }

    printf("Enter something...");
    fgets(data, sizeof(data), stdin);

    // write data into the file.
    fprintf(f, "%s", data);
}

// fseek : moves the file pointer.
// ftell : returns the current position of the file pointer.
// rewind: resets the file position to the beginning.
