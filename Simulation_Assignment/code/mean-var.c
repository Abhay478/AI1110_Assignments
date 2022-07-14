
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double mean(double * a){
    double out = 0;
    for(int i = 0; i < 1000000; i++)
        out += a[i]/1000000;

    return out;
}

double var(double * a, double mu){
    double * ar = malloc(1000000*sizeof(double));
    for(int i = 0; i < 1000000; i++)
        ar[i] = pow(a[i] - mu, 2);

    return mean(ar);
}

int main(){
    FILE * f1 = fopen("../data/uni.dat", "r");
    FILE * f2 = fopen("../data/gau.dat", "r");
    double * a = malloc(1000000*sizeof(double));
    double * b = malloc(1000000*sizeof(double));
    for(int i = 0; i < 1000000; i++){
        fscanf(f1, "%lf", a + i);
        fscanf(f2, "%lf", b + i);
    }    
    double mu = mean(a);
    double sig = var(a, mu);
    printf("Uniform : %lf\t%lf", mu, sig);

    mu = mean(b);
    sig = var(b, mu);
    printf("Gaussian : %lf\t%lf", mu, sig);


}