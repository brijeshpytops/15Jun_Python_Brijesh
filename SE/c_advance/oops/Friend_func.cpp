/* a "friend function" is specific to C++ and does not exist in C. In C++, a friend function is a function that is not a member of a class but still has access to its private and protected members. Friend functions are used when you need to allow a non-member function to access the private data of a class. */

Example :

#include <iostream>
using namespace std;

class ATM{
    int PIN;
    
    public:
    ATM(int a){
        PIN = a;
    }
    
    friend void my_fried_pin(ATM atm);
    
};

void my_fried_pin(ATM atm){
    cout<< atm.PIN;
}

int main() {
    ATM a1(1234);

    my_fried_pin(a1);
    return 0;
}