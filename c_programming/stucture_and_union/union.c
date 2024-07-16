#include <stdio.h>
#include <string.h>

union book{
    char name[100];
    
    int page;
    float price;
};
// }b1, b2;

int main() {
    union book b1, b2;
    b1.page = 30;
    b1.price = 500;
    strcpy(b1.name, "Python");
    printf("B1 Book name is : %s\n", b1.name);
    printf("B1 book pages is : %d\n", b1.page);
    printf("B1 book price is : %f\n\n", b1.price);
    
    b2.page = 60;
    b2.price = 1000;
    strcpy(b2.name, "JAVA");
    printf("B2 Book name is : %s\n", b2.name);
    printf("B2 book pages is : %d\n", b2.page);
    printf("B2 book price is : %f\n\n", b2.price);

    return 0;
}