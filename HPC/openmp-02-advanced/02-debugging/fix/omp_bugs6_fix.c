/******************************************************************************
* FILE: omp_bug6.c
* DESCRIPTION:
*   This program compiles and runs fine, but produces the wrong result.
*   Compare to omp_orphan.c.
* AUTHOR: XXXXXX XXXXXX  6/05
* LAST REVISED: 06/30/05
******************************************************************************/
#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
#define VECLEN 100

float a[VECLEN], b[VECLEN];

float dotprod ()
{
  int i, tid;
  float lsum = 0.0; // FIX 1: Initialize local sum

  tid = omp_get_thread_num();

  //ERROR: #pragma omp for reduction(+:lsum)
  /* FIX: We remove the 'reduction' clause from the orphaned 'for'.
     The threads in the team will still split the iterations 0-99.
     Each thread simply adds to its OWN local 'my_part'.
  */
  #pragma omp for
  for (i=0; i < VECLEN; i++)
    {
    lsum = lsum + (a[i]*b[i]);
    }
  return lsum; // Return the partial sum calculated by this thread
}

int main (int argc, char *argv[]) {
int i;
float sum;

for (i=0; i < VECLEN; i++)
  a[i] = b[i] = 1.0 * i;
sum = 0.0;

//ERROR
//# pragma omp parallel shared(sum)
//  dotprod();

//FIX 2: use reduction instead
#pragma omp parallel reduction(+:sum)
  {
    // Every thread calls dotprod and adds its returned partial sum to the main sum
    sum += dotprod();
  }

printf("Sum = %f\n",sum);

}
