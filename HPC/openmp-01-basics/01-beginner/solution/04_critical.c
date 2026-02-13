#include <stdio.h>
#include <omp.h>

int main() {
    int i, count = 0;

    #pragma omp parallel for
    for(i = 0; i < 100; i++) {
        #pragma omp critical
        count++;
    }

    printf("Count = %d\n", count);
}