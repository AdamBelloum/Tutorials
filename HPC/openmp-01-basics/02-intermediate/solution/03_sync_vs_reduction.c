#include <stdio.h>
#include <omp.h>

int main() {
    long i, sum = 0;

    #pragma omp parallel for
    for(i = 0; i < 1000000; i++) {
        #pragma omp atomic
        sum++;
    }

    printf("Atomic sum: %ld\n", sum);

    sum = 0;

    #pragma omp parallel for reduction(+:sum)
    for(i = 0; i < 1000000; i++)
        sum++;

    printf("Reduction sum: %ld\n", sum);
}
