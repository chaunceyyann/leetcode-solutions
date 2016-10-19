#include <iostream>
#include <string>
#include <vector>
using namespace std;
int numDecodings(string s) {
    int rows = s.size()+1;
    if (rows == 1) return 0;
    vector<int> A(rows, 0);
    A[0] = 1;
    for(int i = 1; i < rows; i++){
        // from one-digit number , range is from 1 to 9
        if (s[i-1] >= '1' && s[i-1] <= '9') A[i] += A[i-1];
        // form two-digit number, the range is from 10 to 26
        if (i-2 >= 0 && s.substr(i-2, 2) <= "26" && s.substr(i-2, 2) >= "10"){
            A[i] += A[i-2];
        }
    }
    return A[rows-1];
}
int main() { 
    cout << numDecodings("152321");
    return 0;
}
