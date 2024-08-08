#include <iostream>
using namespace std;

int main() {
    int age, weight;
    
    cout << "Enter a age and weight: ";
    cin >> age >> weight;
    
    cout<<"age is : "<<age<<endl;
    cout<<"weight is : "<<weight<<endl;
    
    if (age >= 18){
        if(weight >= 50){
            cout<<"You can donate";
        }else{
            cout<<"You can not donate";
        }
    }else{
        cout<<"You can not donate";
    }
    
 
    return 0;
}