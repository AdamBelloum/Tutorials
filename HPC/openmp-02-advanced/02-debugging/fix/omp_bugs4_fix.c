#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
#define N 1048

int main (int argc, char *argv[])
{
 int nthreads, tid, i, j;

 // FIX 1. Allocate on the heap instead of 'double a[N][N]'
    double (*a)[N] = malloc(sizeof(double[N][N]));
    if (a == NULL) {
        fprintf(stderr, "Out of memory!\n");
        return 1;
    }

 // FIX 2. Change 'private(a)' to 'firstprivate(a)' or 
 //    handle pointer logic Since 'a' is a pointer, '
 //    private(a)' would give each thread 
 //    an uninitialized pointer. We keep 'a' shared so   
 //      they all see the same heap address, but this 
 //    logic depends on your goal.

#pragma omp parallel shared(nthreads, a) private(i,j,tid)
  {
    tid = omp_get_thread_num();
    if (tid == 0) {
         nthreads = omp_get_num_threads();
         printf("Number of threads = %d\n", nthreads);
    }
    for (i=0; i<N; i++)
     for (j=0; j<N; j++)
      a[i][j] = tid + i + j;

   printf("Th %d done.Last element= %f\n",tid,a[N-1][N-1]);
  }

  free(a); // 3. Don't forget to free!
  return 0;
}

