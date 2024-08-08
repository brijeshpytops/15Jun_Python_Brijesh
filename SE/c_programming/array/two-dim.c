#include <stdio.h>

int main() {
    int matrix1[3][2] = {
        {1,2},
        {3,4},
        {5,6}
    };
    
    int matrix2[3][2] = {
        {11,22},
        {33,44},
        {55,66}
    };
    
    // access element
    // printf("%d", matrix1[1][1]);
    
    // find the length of two dim array
    int len_outer = sizeof(matrix1)/sizeof(matrix1[0]);
    int len_inner = sizeof(matrix1[0])/sizeof(matrix1[0][0]);
    // printf("%d", len);
    
    
    printf("Matrix-1:\n");
    for(int row = 0; row<len_outer; row++){
        for(int col = 0; col<len_inner; col++){
            printf("%d ", matrix1[row][col]);
        }
        printf("\n");
    }
    
    printf("Matrix-2:\n");
    for(int row = 0; row<len_outer; row++){
        for(int col = 0; col<len_inner; col++){
            printf("%d ", matrix2[row][col]);
        }
        printf("\n");
    }
    
    printf("Matrix-1 + Matrix-2:\n");
    for(int row = 0; row<len_outer; row++){
        for(int col = 0; col<len_inner; col++){
            printf("%d ", matrix1[row][col] + matrix2[row][col]);
        }
        printf("\n");
    }
    return 0;
}



#include <stdio.h>

int main() {
    int matrix1[3][2] = {
        {1,2},
        {3,4},
        {5,6}
    };
    
    int matrix2[3][2] = {
        {11,22},
        {33,44},
        {55,66}
    };
    
    // access element
    // printf("%d", matrix1[1][1]);
    
    // find the length of two dim array
    int len_outer = sizeof(matrix1)/sizeof(matrix1[0]);
    int len_inner = sizeof(matrix1[0])/sizeof(matrix1[0][0]);
    // printf("%d", len);
    
    
    printf("Matrix-1:\n");
    for(int row = 0; row<len_outer; row++){
        for(int col = 0; col<len_inner; col++){
            printf("%d ", matrix1[row][col]);
        }
        printf("\n");
    }
    
    printf("Matrix-2:\n");
    for(int row = 0; row<len_outer; row++){
        for(int col = 0; col<len_inner; col++){
            printf("%d ", matrix2[row][col]);
        }
        printf("\n");
    }
    
    printf("Matrix-1 * Matrix-2:\n");
    for(int row = 0; row<len_outer; row++){
        for(int col = 0; col<len_inner; col++){
            printf("%d ", matrix1[row][col] * matrix2[row][col]);
        }
        printf("\n");
    }
    return 0;
}


#include<stdio.h>
int main() {
    int matrix[3][2] = {
        {1,2},
        {3,4},
        {5,6}
    };
    
    int len_outer = sizeof(matrix)/sizeof(matrix[0]);
    int len_inner = sizeof(matrix[0])/sizeof(matrix[0][0]);
    
    int total = 0;
    for(int row = 0; row<len_outer; row++){
        for(int col = 0; col<len_inner; col++){
            total += matrix[row][col];
        }
    }
    printf("Total = %d", total);
    
    
    return 0;
}



#include<stdio.h>
int main() {
    int subs[10];
    
    for(int start = 0; start<5; start++){
        printf("Enter sub-%d", start+1);
        scanf("%d", &subs[start]);
    }
    
    int total = 0;
    for(int start = 0; start<5; start++){
        printf("Enter sub-%d : marks: %d\n", start+1, subs[start]);
        total+=subs[start];
    }
    
    float res = total*100;
    
    printf("Total Percentage is : %f", res/500);
}