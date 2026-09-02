#include <stdio.h>
#include <omp.h>
#include <stdlib.h>

int main() {
    int i;
    int N = 20;

    #pragma omp parallel for private(i)
    for(i = 0; i < N; i++)
        printf("i=%d (thread=%d)\n", i, omp_get_thread_num());

    return 0;
}
