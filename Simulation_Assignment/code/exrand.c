#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int  main(void) //main function begins
{
 
    //Uniform random numbers
    // uniform("../data/uni.dat", 1000000);

    // //Gaussian random numbers
    // gaussian("../data/gau.dat", 1000000);

    // //Exponential random numbers
    // exponential("../data/exp.dat", 1000000, 2);

    // //Triangular random numbers
    // triang("../data/tri.dat", 1000000);

    // //More exponential random numbers
    // gss("../data/gss.dat", 1000000, 2);

    // //Raleigh
    // raleigh("../data/ral.dat", 1000000, 2);

    // //Signal
    // plusminus("../data/plm.dat", 1000000);

    // //Noise
    // noise("../data/noi.dat", "../data/plm.dat", 1000000);

    //Conditional
    conditional("../data/con.dat");
    
    return 0;
}

