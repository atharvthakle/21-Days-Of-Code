#include <iostream>
#include <vector>
using namespace std;

int findIndex(const vector<int>& arr, int m) {
    for (int i = 0; i < arr.size(); ++i) {
        if (arr[i] == m) {
            return i;
        }
    }
    return -1;
}

int main() {
    int n;
    cin >> n;

    vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    int m;
    cin >> m;

    int index = findIndex(arr, m);
    cout << index << endl;

    return 0;
}
