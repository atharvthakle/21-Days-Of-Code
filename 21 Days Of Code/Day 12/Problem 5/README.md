# Problem 5

Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle

Your implementation should support following operations :

MyCircularQueue(k) : Constructor, set the size of the queue to be k.

Front : Get the front item from the queue. If the queue is empty, return -1.

Rear : Get the last item from the queue. If the queue is empty, return -1.

enQueue(value) : Insert an element into the circular queue. Return true if the operation is successful.

deQueue() : Delete an element from the circular queue. Return true if the operation is successful.

isEmpty() : Checks whether the circular queue is empty or not.

isFull() : Checks whether the circular queue is full or not.

## Input Format

The First Line of the Input contains 'size' of the Circular Queue. Then Follow the Instructions--

Enqueue()

Dequeue()

Front()

Rear()

IsEmpty()

IsFull() Press any other number to exit. (Its a loop statement, which would work until you press any other number)

### Constraints

All values will be in the range of [0, 1000].

The number of operations will be in the range of [1, 1000]

## Output Format

Output would be a value depending on the called function.

### Sample Input

3

1

10

1

20

1

30

2

3

9

### Sample Output

true

true

true

true

20

## Explanation

Three Enqueue Operations : 10 20 30 (View of Queue i.e. Front is 10 and Rear is 30)

Dequeue 10

Current Status of Queue : 20 30
Front(): 20 //
