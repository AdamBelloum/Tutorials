#include <stdio.h>
#include <omp.h>

void work(int n) {
    if (n < 1) return;
    #pragma omp task
    work(n-1);
}

int main() {
    #pragma omp parallel
    {
        #pragma omp single
        work(10);
    }
    return 0;
}
