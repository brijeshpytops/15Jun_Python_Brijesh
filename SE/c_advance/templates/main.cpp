/*
Templates in C++ provide a way to create generic functions and classes. They allow you to define a blueprint that can work with any data type. Templates are essential for creating code that is reusable and type-safe, especially when dealing with collections, algorithms, or other constructs that can operate on various types.

Function Templates
A function template allows you to create a function that can operate on different data types without rewriting the entire function for each type.


#include <iostream>
using namespace std;

// Function template
template <typename T>
T add(T a, T b) {
    return a + b;
}

int main() {
    cout << "Addition of integers: " << add(5, 3) << endl;          // Output: 8
    cout << "Addition of doubles: " << add(5.5, 3.3) << endl;      // Output: 8.8
    return 0;
}

Class Templates
A class template allows you to create a class that can operate with any data type.


#include <iostream>
using namespace std;

// Class template
template <typename T>
class Box {
private:
    T value;

public:
    // Constructor
    Box(T val) : value(val) {}

    // Member function to get the value
    T getValue() const {
        return value;
    }
};

int main() {
    Box<int> intBox(123);
    Box<double> doubleBox(456.789);

    cout << "Integer value: " << intBox.getValue() << endl;        // Output: 123
    cout << "Double value: " << doubleBox.getValue() << endl;      // Output: 456.789

    return 0;
}

*/