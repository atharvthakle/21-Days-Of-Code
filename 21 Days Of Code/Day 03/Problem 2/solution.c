// In a cozy neighborhood nestled among bustling streets, Mr. Blocks, the friendly local baker, greeted the dawn with the aroma of freshly baked buns wafting from his shop. Meanwhile, Mayank, a perpetually forgetful fellow with a heart of gold, stirred from his slumber with a start.

After waking up at hh:mm, Mayank realised that he had forgotten to feed his only cat for yet another time (guess why there's only one cat). The cat's current hunger level is H points, moreover each minute without food increases his hunger by D points.

At any time Mayank can visit the store where tasty buns are sold (you can assume that is doesn't take time to get to the store and back). One such bun costs C roubles and decreases hunger by N points. Since the demand for bakery drops heavily in the evening, there is a special 20% discount for buns starting from 20:00 (note that the cost might become rational). Of course, buns cannot be sold by parts.

Determine the minimum amount of money Mayank has to spend in order to feed his cat. The cat is considered fed if its hunger level is less than or equal to zero.
Note : Discount works from 20:00 till 23:59.

Input Format
The first line contains two integers hh and mm (00 ≤ hh ≤ 23, 00 ≤ mm ≤ 59) — the time of Mayank's awakening.

The second line contains four integers H, D, C and N (1 ≤ H ≤ 105, 1 ≤ D, C, N ≤ 102).

Constraints
(00 ≤ hh ≤ 23, 00 ≤ mm ≤ 59),
(1 ≤ H ≤ 105, 1 ≤ D, C, N ≤ 102)

Output Format
Output the minimum amount of money to with four decimal digits. It means if your answer it 2 then you should print 2.0000 and similarly if your output is 5.67 you should print 5.6700 and same. Output should be upto 4 decimal digits.


Note : While Taking Input and Output Ignore Test case Input No and Test Case Output No, These are for your understanding.

Sample Input
Test Case Input 1: 
19 00
255 1 100 1

Test Case Input 2: 
17 41
1000 6 15 11
Sample Output
Test Case Output 1:
25200.0000

 Test Case Output 2:
1365.0000
Explanation
In the first sample Mayank can visit the store at exactly 20:00. The cat's hunger will be equal to 315, hence it will be necessary to purchase 315 buns. The discount makes the final answer 25200 roubles.

In the second sample it's optimal to visit the store right after he wakes up. Then he'll have to buy 91 bins per 15 roubles each and spend a total of 1365 roubles. //


#include <stdio.h>
#include <math.h>

int main() {
    int hh, mm, H, D, C, N;
    scanf("%d %d", &hh, &mm);
    scanf("%d %d %d %d", &H, &D, &C, &N);

    // Calculate time until discount starts
    int minutesUntilDiscount = fmax(0, (20 - hh) * 60 - mm);

    // Calculate hunger level at discount
    int hungerAtDiscount = H + minutesUntilDiscount * D;

    // Calculate buns needed and cost without waiting
    int bunsNeededNow = (H + N - 1) / N;
    double costNow = bunsNeededNow * C;

    // Calculate buns needed and cost with discount
    int bunsNeededAtDiscount = (hungerAtDiscount + N - 1) / N;
    double costAtDiscount = bunsNeededAtDiscount * C * 0.8;

    // Determine minimum cost
    double minCost = fmin(costNow, costAtDiscount);

    // Set precision and output result
    printf("%.4lf\n", minCost);

    return 0;
}
