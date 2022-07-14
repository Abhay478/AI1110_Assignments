//Function declaration
double **createMat(int m,int n);
void readMat(double **p, int m,int n);
void print(double **p,int m,int n);
double **loadtxt(char *str,int m,int n);
double linalg_norm(double **a, int m);
double **linalg_sub(double **a, double **b, int m, int n);
double **linalg_inv(double **mat, int m);
double **matmul(double **a, double **b, int m, int n, int p);
double **transpose(double **a,  int m, int n);
void uniform(char *str, int len);
void gaussian(char *str, int len);
double mean(char *str);
//End function declaration


//Defining the function for matrix creation
double **createMat(int m,int n)
{
 int i;
 double **a;
 
 //Allocate memory to the pointer
a = (double **)malloc(m * sizeof( *a));
    for (i=0; i<m; i++)
         a[i] = (double *)malloc(n * sizeof( *a[i]));

 return a;
}
//End function for matrix creation


//Defining the function for reading matrix 
void readMat(double **p, int m,int n)
{
 int i,j;
 for(i=0;i<m;i++)
 {
  for(j=0;j<n;j++)
  {
   scanf("%lf",&p[i][j]);
  }
 }
}
//End function for reading matrix

//Read  matrix from file
double **loadtxt(char *str,int m,int n)
{
FILE *fp;
double **a;
int i,j;


a = createMat(m,n);
fp = fopen(str, "r");

 for(i=0;i<m;i++)
 {
  for(j=0;j<n;j++)
  {
   fscanf(fp,"%lf",&a[i][j]);
  }
 }
//End function for reading matrix from file

fclose(fp);
 return a;

}


//Defining the function for printing
void print(double **p, int m,int n)
{
 int i,j;

 for(i=0;i<m;i++)
 {
  for(j=0;j<n;j++)
  printf("%lf ",p[i][j]);
 printf("\n");
 }
}
//End function for printing

//Defining the function for norm

double linalg_norm(double **a, int m)
{
int i;
double norm=0.0;

 for(i=0;i<m;i++)
 {
norm = norm + a[i][0]*a[i][0];
}
return sqrt(norm);

}
//End function for norm

//Defining the function for difference of matrices

double **linalg_sub(double **a, double **b, int m, int n)
{
int i, j;
double **c;
c = createMat(m,n);

 for(i=0;i<m;i++)
 {
  for(j=0;j<n;j++)
  {
c[i][j]= a[i][j]-b[i][j];
  }
 }
return c;

}
//End function for difference of matrices

//Defining the function for inverse of 2x2 matrix


double **linalg_inv(double **mat, int m)
{
double **c, det;
c = createMat(m,m);

det = mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0];

c[0][0] = mat[1][1]/det;
c[0][1] = -mat[1][0]/det;
c[1][0] = -mat[0][1]/det;
c[1][1] = mat[0][0]/det;

return c;

}
// End  function for inverse of 2x2 matrix


//Defining the function for difference of matrices

double **matmul(double **a, double **b, int m, int n, int p)
{
int i, j, k;
double **c, temp =0;
c = createMat(m,p);

 for(i=0;i<m;i++)
 {
  for(k=0;k<p;k++)
  {
    for(j=0;j<n;j++)
    {
	temp= temp+a[i][j]*b[j][k];
    }
	c[i][k]=temp;
	temp = 0;
  }
 }
return c;

}
//End function for difference of matrices

//Defining the function for transpose of matrix

double **transpose(double **a,  int m, int n)
{
	int i, j;
	double **c;
	c = createMat(n,m);
	for(i=0;i<n;i++){
		for(j=0;j<m;j++){
			c[i][j]= a[j][i];
  		}
	}
	return c;

}


void uniform(char * str, int len)
{
int i;
FILE *fp;

fp = fopen(str,"w");
//Generate numbers
for (i = 0; i < len; i++)
{
fprintf(fp,"%lf\n",(double)rand()/RAND_MAX);
}
fclose(fp);

}
//End function for generating uniform random numbers

void exponential(char * fn, int n, double l){
    FILE * f = fopen(fn, "w");

    for(int i = 0; i < n; i++)
        fprintf(f, "%lf\n", -l * log(1 - (double)random()/RAND_MAX));

	fclose(f);

}

void gss(char * fn, int n, int v)
{
	FILE * f = fopen(fn, "w");

	double sum = 0;
	double temp = 0;
	for(int i = 0; i < n; i++){
		sum = 0;
		for(int j = 0; j < v; j++){
			temp = 0;
			for (int k = 0; k < 12; k++)
				temp += (double)rand()/RAND_MAX;

			temp-=6;
			sum += temp*temp;
		}
		fprintf(f, "%lf\n", sum);
	}

	fclose(f);
}

void triang(char * fn, int n){
	FILE * f = fopen(fn, "w");

	double u1, u2;
	for(int i = 0; i < n; i++){
		u1 = (double)random()/RAND_MAX; 
		u2 = (double)random()/RAND_MAX;
		double t = u1 + u2;
		//adding 2 uniform variables
        fprintf(f, "%lf\n", t);
	}
	fclose(f);

}
//Defining the function for calculating the mean of random numbers
double mean(char *str)
{
int i=0,c;
FILE *fp;
double x, temp=0.0;

fp = fopen(str,"r");
//get numbers from file
while(fscanf(fp,"%lf",&x)!=EOF)
{
//Count numbers in file
i=i+1;
//Add all numbers in file
temp = temp+x;
}
fclose(fp);
temp = temp/(i-1);
return temp;

}
//End function for calculating the mean of random numbers

//Defining the function for generating Gaussian random numbers
void gaussian(char *str, int len)
{
int i,j;
double temp;
FILE *fp;

fp = fopen(str,"w");
//Generate numbers
for (i = 0; i < len; i++)
{
temp = 0;
for (j = 0; j < 12; j++)
{
temp += (double)rand()/RAND_MAX;
}
temp-=6;
fprintf(fp,"%lf\n",temp);
}
fclose(fp);

}
//End function for generating Gaussian random numbers

void raleigh(char * fn, int n, int v)
{
	FILE * f = fopen(fn, "w");

	double sum = 0;
	double temp = 0;
	for(int i = 0; i < n; i++){
		sum = 0;
		for(int j = 0; j < v; j++){
			temp = 0;
			for (int k = 0; k < 12; k++)
				temp += (double)rand()/RAND_MAX;

			temp-=6;
			sum += temp*temp;
		}
		fprintf(f, "%lf\n", sqrt(sum));
	}

	fclose(f);
}

void plusminus(char * fn, int n){
	int i;
FILE * f = fopen(fn, "w");
//Generate numbers
for (i = 0; i < n; i++){
	fprintf(f,"%d\n",((double)rand()/RAND_MAX) > 0.5 ? 1 : -1);
}
fclose(f);
}

void noise(char * fn_y, char * fn_x,  int n)
{
	double temp, sig;
	int in;
	FILE * f = fopen(fn_y, "w");
	FILE * fp = fopen(fn_x, "r");
	for(int i = 0; i < n; i++){
		temp = 0;
		for (int j = 0; j < 12; j++){
			temp += (double)rand()/RAND_MAX;
		}
		temp-=6;
		fscanf(fp, "%d", &in);
		sig = 5 * in;
		sig += temp;

		fprintf(f, "%lf\n", sig);
	}
	fclose(f);
}

void conditional(char * fn)
{
	FILE * f = fopen(fn, "w");
	FILE * f_plm = fopen("../data/plm.dat", "r");
	FILE * f_gau = fopen("../data/gau.dat", "r");

	double N;
	int X;

	for(int i = 1; i <= 100; i++){
    	for(int j = 0; j < 10000; j++){
			fscanf(f_gau, "%lf", &N);
			fscanf(f_plm, "%d", &X);
			double A = sqrt(-(double)i/10 * log((double)random()/RAND_MAX));

			double Y = A*X + N;
			
        	fprintf(f, "%lf\t", Y);
		}fprintf(f, "\n");
		// printf("%d\n", i);
	}
	fclose(f);
}

