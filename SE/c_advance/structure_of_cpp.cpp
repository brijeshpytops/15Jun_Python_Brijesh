// structure of c++
// documentation section
// linking section
// global declartion section
// function declaration section
// main function declaration section
// sub function declaration section

// documentation section
// write a program to find area of circle

// linking section

#include <iostream> // for input/output operations
using namespace std;

// global declartion section
const float PI = 3.14;

// function declaration section
int circle_area(){};

// main function declaration section

int main(){
    int radius;
    cout << "Enter radius of circle: ";
    cin >> radius;

    // calling sub function to calculate area
    int area = circle_area(radius);

    cout << "Area of circle: " << area << endl;

    return 0;
}

// sub function declaration section

int circle_area(int radius){
    return PI * radius * radius;
}