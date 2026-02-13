#include <stdio.h>
#include <omp.h>

int main() {
    int i;
    int N = 20;
    int A[20];

    #pragma omp parallel for
    for(i = 0; i < N; i++)
        A[i] = i * i;

    for(i = 0; i < N; i++)
        printf("%d ", A[i]);
    printf("\n");
}
