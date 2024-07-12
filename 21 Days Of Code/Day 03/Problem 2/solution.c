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
