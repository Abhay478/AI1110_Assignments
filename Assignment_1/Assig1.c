
#include <stdio.h>

#define k -2
int f(int x)
{
    return x*x*x + (k*x + 8)*x + k;
}
/*
To verify the solution, we prove the givens and the results of the solution are, as a whole, consistent with the remainder theorem.
We know the remainders after division by (x + 1) and (x - 2) are -13 and 14 respectively. 
We know that the value of k is -2 (as hash-defined above)
*/
int main()
{
    //if the solution violates remainder theorem, prints false
    if(f(-1) != -13 || f(2) != 14) printf("False.\n"); 
    else printf("True.\n");

    return 0;
}