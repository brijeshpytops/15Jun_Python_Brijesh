#include <iostream>
using namespace std;

int main() {
    int num1, num2, res;
    
    cout << "Enter a num1 and num2: ";
    cin >> num1 >> num2;
    
    cout<<"Num1 is : "<<num1<<endl;
    cout<<"Num2 is : "<<num2<<endl;
    
    res = num1 + num2;
    // res = num1 - num2;
    res = num1 * num2;
    cout<< "Total = "<<res;
    return 0;
}