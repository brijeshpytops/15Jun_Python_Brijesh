#include <iostream>
using namespace std;

int main() {
    try {
        float bal = 10000, wb;
       
        cout << "Enter withdrow balance: ";
        cin >> wb;

        if (wb > bal) {
            throw runtime_error("Insufficent balance");
        }else{
            cout<<"Wthdrow successfully done."<<endl;
            cout<<"Total remaining bal is: "<<bal-wb<<endl;
        }
    } catch (const runtime_error &e) {
        cerr << "Runtime error: " << e.what() << endl;
    } catch (...) {
        cerr << "An unexpected error occurred!" << endl;
    }

    return 0;
}
