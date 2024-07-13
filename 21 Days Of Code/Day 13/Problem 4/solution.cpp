#include <iostream>
#include <queue>
#include <string>
using namespace std;

class node {
public:
    int data;
    node* left;
    node* right;

    node(int d) {
        data = d;
        left = NULL;
        right = NULL;
    }
};

node* build(string s) {
    if (s == "true") {
        int d;
        cin >> d;
        node* root = new node(d);
        string l;
        cin >> l;
        if (l == "true") {
            root->left = build(l);
        }
        string r;
        cin >> r;
        if (r == "true") {
            root->right = build(r);
        }
        return root;
    }
    return NULL;
}

pair<int, bool> isHeightBalancedOptimized(node* root) {
    if (root == NULL) {
        return make_pair(0, true);
    }

    pair<int, bool> left = isHeightBalancedOptimized(root->left);
    pair<int, bool> right = isHeightBalancedOptimized(root->right);

    int height = 1 + max(left.first, right.first);
    bool balanced = left.second && right.second && abs(left.first - right.first) <= 1;

    return make_pair(height, balanced);
}

int main() {
    node* root = build("true");

    cout << boolalpha << isHeightBalancedOptimized(root).second << endl;

    return 0;
}
