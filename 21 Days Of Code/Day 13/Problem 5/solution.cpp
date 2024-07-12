// Given a binary tree print all nodes that don’t have a sibling

Input Format
Enter the values of all the nodes in the binary tree in pre-order format where true suggest the node exists and false suggests it is NULL

Constraints
None

Output Format
Display all the nodes which do not have a sibling in a space separated manner

Sample Input
50 true 12 true 18 false false false false
Sample Output
12 18 //


#include <iostream>
#include <queue>
#include <vector>

using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;
};

Node* createNode(int data) {
    Node* newNode = new Node();
    if (!newNode) {
        cout << "Memory error\n";
        return NULL;
    }
    newNode->data = data;
    newNode->left = newNode->right = NULL;
    return newNode;
}

Node* buildTree(vector<string>& values, int& i) {
    if (values[i] == "true") {
        int data = stoi(values[++i]);
        Node* newNode = createNode(data);
        newNode->left = buildTree(values, ++i);
        newNode->right = buildTree(values, ++i);
        return newNode;
    }
    return NULL;
}

void printNodesWithoutSiblings(Node* root) {
    if (root == NULL) {
        return;
    }
    if (root->left != NULL && root->right == NULL) {
        cout << root->left->data << " ";
    }
    if (root->right != NULL && root->left == NULL) {
        cout << root->right->data << " ";
    }
    printNodesWithoutSiblings(root->left);
    printNodesWithoutSiblings(root->right);
}

int main() {
    int n;
    cin >> n;
    vector<string> values(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i];
    }
    int i = 0;
    Node* root = buildTree(values, i);
    printNodesWithoutSiblings(root);
    return 0;
}