#include <iostream>
#include <vector>

using namespace std;

class MyCircularQueue {
private:
    vector<int> queue;
    int front;
    int rear;
    int size;
    int count;

public:
    MyCircularQueue(int k) {
        queue.resize(k);
        size = k;
        front = 0;
        rear = -1;
        count = 0;
    }

    bool enQueue(int value) {
        if (isFull())
            return false;
        rear = (rear + 1) % size;
        queue[rear] = value;
        count++;
        return true;
    }

    bool deQueue() {
        if (isEmpty())
            return false;
        front = (front + 1) % size;
        count--;
        return true;
    }

    int Front() {
        if (isEmpty())
            return -1;
        return queue[front];
    }

    int Rear() {
        if (isEmpty())
            return -1;
        return queue[rear];
    }

    bool isEmpty() {
        return count == 0;
    }

    bool isFull() {
        return count == size;
    }
};

int main() {
    int k;
    cin >> k;

    MyCircularQueue obj(k);
    int operation;

    while (true) {
        cin >> operation;
        switch (operation) {
            case 1: {
                int value;
                cin >> value;
                cout << (obj.enQueue(value) ? "true" : "false") << endl;
                break;
            }
            case 2: {
                cout << (obj.deQueue() ? "true" : "false") << endl;
                break;
            }
            case 3: {
                cout << obj.Front() << endl;
                break;
            }
            case 4: {
                cout << obj.Rear() << endl;
                break;
            }
            case 5: {
                cout << (obj.isEmpty() ? "true" : "false") << endl;
                break;
            }
            case 6: {
                cout << (obj.isFull() ? "true" : "false") << endl;
                break;
            }
            default:
                return 0;
        }
    }

    return 0;
}
