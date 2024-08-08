#include <iostream>
using namespace std;

class Rectangle {
private:
    int width;
    int height;

public:
    // Constructor
    Rectangle(int width, int height) {
        // Using this to differentiate between member variables and parameters
        this->width = width;
        this->height = height;
    }

    // Member function to calculate area
    int area() {
        return this->width * this->height;
    }

    // Member function to set dimensions
    void setDimensions(int width, int height) {
        this->width = width;
        this->height = height;
    }

    // Member function to print dimensions
    void printDimensions() {
        cout << "Width: " << this->width << ", Height: " << this->height << endl;
    }

    // Returning the object itself using this
    Rectangle* getSelf() {
        return this;
    }
};

int main() {
    // Creating an object of Rectangle
    Rectangle rect(10, 5);

    // Accessing member functions
    rect.printDimensions();            // Output: Width: 10, Height: 5
    cout << "Area: " << rect.area() << endl;  // Output: Area: 50

    // Modifying dimensions
    rect.setDimensions(7, 3);
    rect.printDimensions();            // Output: Width: 7, Height: 3
    cout << "Area: " << rect.area() << endl;  // Output: Area: 21

    // Using this to return the object itself
    Rectangle* ptr = rect.getSelf();
    ptr->printDimensions();            // Output: Width: 7, Height: 3

    return 0;
}
