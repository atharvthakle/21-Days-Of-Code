# Problem 4

Write a program that works as a simple calculator.

• It reads a character (ch)

• If ch is among '+', '-', '*', '/' or '%' it furthur takes two numbers (N1 and N2 as input). It then performs appropriate appropriate operation between numbers and print the number.

• If ch is 'X' or 'x', the program terminates.

• If ch is any other character, the program should print 'Invalid operation. Try again.' and seek inputs again (starting from character).

Write code to achieve above functionality.

## Input Format

Constraints

0 <= Input integers <= 100000000

( It is assured that the second integer provided for division and modulo operations will not be 0. )

## Output Format

Output a single integer output for the operations in a new line each.

## Sample Input

* (multiplication star)

1 

2 

/

4 

2 

+ (addition plus)

3 

2 

; 

X

## Sample Output

2 

2 

5 

Invalid operation. Try again.

## Explanation

Maybe use a do-while.
