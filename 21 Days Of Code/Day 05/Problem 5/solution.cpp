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
