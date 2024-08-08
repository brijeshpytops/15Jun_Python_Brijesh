#include <iostream>
using namespace std;

int main() {
    
    while(1){
         int age, weight;
    
    cout << "Enter a age: ";
    cin >> age;
    
    // cout<<"age is : "<<age<<endl;
    // cout<<"weight is : "<<weight<<endl;
    if (age >= 18){
         cout << "Enter a weight: ";
        cin >> weight;
        if(weight >= 50){
            cout<<"You can donate"<<endl;
        }else{
            cout<<"You can not donate"<<endl;
        }
    }else{
        cout<<"You can not donate"<<endl;
    }
    }
    return 0;
}