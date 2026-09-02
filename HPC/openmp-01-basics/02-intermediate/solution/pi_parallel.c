#include <stdio.h>
#include <omp.h>
int main(){
    long long N = 1000000;
    double step = 1.0/N, sum=0.0;
    #pragma omp parallel for reduction(+:sum)
    for(long long i=0;i<N;i++){
        double x=(i+0.5)*step;
        sum += 4.0/(1.0+x*x);
    }
    printf("PI=%f\n", sum*step);
    return 0;
}
