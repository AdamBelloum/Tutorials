/******************************************************************************
* FILE: omp_bug1fix.c
* DESCRIPTION:
*   This is a corrected version of the omp_bug1.c example. Corrections
*   include removing all statements between the parallel for construct and
*   the actual for loop, and introducing logic to preserve the ability to 
*   query a thread's id and print it from inside the for loop.
* AUTHOR: Blaise Barney  5/99
* LAST REVISED: 04/06/05
******************************************************************************/
#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
#define N       50
#define CHUNKSIZE   5

int main (int argc, char *argv[])
{
int i, chunk, tid;
float a[N], b[N], c[N];

/* Some initializations */
for (i=0; i < N; i++)
  a[i] = b[i] = i * 1.0;
chunk = CHUNKSIZE;

#pragma omp parallel for shared(a,b,c,chunk) private(i,tid) schedule(static,chunk)
// Error: the follwing block opening is not allowed "{" compiler is exepected to find "for"
// {
// Error: the following  instruction cannot be placed here compiler is expecting "for"
//        the statement should be moved in the for loop
// tid = omp_get_thread_num(); 
  for (i=0; i < N; i++)
    {
    //FIX:
    tid = omp_get_thread_num();
    c[i] = a[i] + b[i];
    printf("tid= %d i= %d c[i]= %f\n", tid, i, c[i]);
    }
    /* end of parallel for construct */
//}
}
