#include <stdio.h>

// Inline function definition
inline int add(int a, int b) {
    return a + b;
}

int main() {
    int result = add(3, 4);
    printf("The result is %d\n", result);
    return 0;
}
