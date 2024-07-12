// Take as input N, a number. Take N more inputs and store that in an array. Write a recursive function which inverses the array. Print the values of inverted array

Input Format
Enter a number N and take N more inputs

Constraints
None

Output Format
Display the values of the inverted array in a space separated manner

Sample Input
5
0 2 4 1 3
Sample Output
0 3 1 4 2
Explanation
Swap element with index

for eg : element 4 at index 2 becomes element 2 at index 4 //


#include <iostream>
#include <vector>
using namespace std;

// Function to reverse the array with index swapping
vector<int> reverseArray(const vector<int>& arr, int N) {
    vector<int> result(N);
    for (int i = 0; i < N; ++i) {
        result[arr[i]] = i;
    }
    return result;
}

int main() {
    int N;
    // Read input size of array
    cin >> N;

    vector<int> array(N);
    // Read array elements
    for (int i = 0; i < N; ++i) {
        cin >> array[i];
    }

    // Get the reversed array
    vector<int> reversedArray = reverseArray(array, N);

    // Print the reversed array
    for (int i = 0; i < N; ++i) {
        cout << reversedArray[i] << " ";
    }
    cout << endl;

    return 0;
}