#include <stdio.h>

int main() {

    // create an array of students[define and initialize]
    float students[] = {56, 67, 45, 79, 97, 86, 57, 54, 87};
    // students[6] = 75; // update
    // printf("%f", students[6]); // access single student data from array
    

    // find the array length of students
    int length = sizeof(students)/sizeof(students[0]);
    // printf("Array length is : %d", length);
    
    // access all the elements of the array
    for(int start = 0; start<length; start++){
        printf("Student-%d : %.1f\n",start+1, students[start]);
    }
    return 0;
}