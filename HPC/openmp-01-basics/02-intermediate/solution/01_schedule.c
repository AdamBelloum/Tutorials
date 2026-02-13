#include <stdio.h>
#include <omp.h>

int main() {
    int i;
    int N = 20;

    #pragma omp parallel for schedule(dynamic,2)
    for(i = 0; i < N; i++) {
        printf("i=%d from thread=%d\n", i, omp_get_thread_num());
    }
}
