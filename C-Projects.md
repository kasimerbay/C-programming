### Calculate the sum of the lower triangular entries of a multidimensional matrix.
```C
#include <stdio.h>

void read_array(int a[][20],int R,int C){
    
int i,j;

    for(i=0;i<R;i++){

        for(j=0;j<C;j++){

            scanf("%d",&a[i][j]);

        }

    }

}

void print_array(int a[][20],int R,int C){

    int i,j;

    for(i=0;i<R;i++){

        for(j=0;j<C;j++){

            printf("%d ",a[i][j]);

        }
        printf("\n");

    }

}
int main() {

    int R,C,i,j,arr[20][20],term=0;

    scanf("%d %d",&R,&C);

    read_array(arr,R,C);

    for(i=R-1;i>=0;i--){

        for(j=C-1;j>=C-1-i;j--){

            printf("%d\n",arr[i][j]);

          term+=arr[i][j];
  
        }

    }

    printf("%d\n",term);

    print_array(arr,R,C);

    return 0;

}
```
# Median Calculation
```C
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
float median(int a[50],int N){
    float median;
    if(N%2==1){
        median=a[N/2];
    }
    else{
        median=1.0*(a[N/2]+a[(N-2)/2])/2;
    }
    return median;
}
//Çeyrekler Açýklýðý
int main() {
int i,N;
int a[100]={},b[100]={};
    scanf("%d",&N);
//Take two arrays: First the elements, second the frequencies in the corresponding indexes.
    for(i=0;i<N;i++){
        scanf("%d",&a[i]);}
    for(i=0;i<N;i++){
        scanf("%d",&b[i]);}
//to define the new array find its size first.
//it is the sum of the elements in the second array.
int N2=0;
    for(i=0;i<N;i++){
        N2+=b[i];
        }
//Fill the S array with the given frequencies.
    int s[500]={},j,k=0;
    for(i=0;i<N;i++){
        for(j=0;j<b[i];j++){
            s[k]=a[i];
            k++;
        }
    }
//Selective sort.
    int temp;
    for(i=0;i<N;i++){
      for(j=i+1;j<N;j++){
         if(s[i]>s[j]){
            temp=a[i];
            s[i]=a[j];
            s[j]=temp;
         }
      }
    }
//Define two new arrays for quantiles.
    int c[250]={},d[250]={};
//Divide S to two new array.
     if(N2%2==1){
        for(i=0;i<N2/2;i++){
            c[i]=s[i];
        }
        for(i=0;i<N2/2;i++){
            d[i]=s[(N2/2)+1+i];
        }
    }
    else{
        for(i=0;i<N2/2;i++){
            c[i]=s[i];
        }
        for(i=0;i<N2/2;i++){
            d[i]=s[(N2/2)+i];
        }
    }
//Use the median Function to find newest arrays median values.
    float result;
    result = median(d,N2/2) - median(c,N2/2);
    printf("%.1f",result);
    return 0;
}
```
---
# Quantiles
```C
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
float median(int a[50],int N){
    float median;
    if(N%2==1){
        median=a[N/2];
    }
    else{
        median=1.0*(a[N/2]+a[(N-2)/2])/2;
    }
    return median;
}
//Çeyrekler Açýklýðý
int main() {
int i,N;
int a[100]={},b[100]={};
    scanf("%d",&N);
//Take two arrays: First the elements, second the frequencies in the corresponding indexes.
    for(i=0;i<N;i++){
        scanf("%d",&a[i]);}
    for(i=0;i<N;i++){
        scanf("%d",&b[i]);}
//to define the new array find its size first.
//it is the sum of the elements in the second array.
int N2=0;
    for(i=0;i<N;i++){
        N2+=b[i];
        }
//Fill the S array with the given frequencies.
    int s[500]={},j,k=0;
    for(i=0;i<N;i++){
        for(j=0;j<b[i];j++){
            s[k]=a[i];
            k++;
        }
    }
//Selective sort.
    int temp;
    for(i=0;i<N;i++){
      for(j=i+1;j<N;j++){
         if(s[i]>s[j]){
            temp=a[i];
            s[i]=a[j];
            s[j]=temp;
         }
      }
    }
//Define two new arrays for quantiles.
    int c[250]={},d[250]={};
//Divide S to two new array.
     if(N2%2==1){
        for(i=0;i<N2/2;i++){
            c[i]=s[i];
        }
        for(i=0;i<N2/2;i++){
            d[i]=s[(N2/2)+1+i];
        }
    }
    else{
        for(i=0;i<N2/2;i++){
            c[i]=s[i];
        }
        for(i=0;i<N2/2;i++){
            d[i]=s[(N2/2)+i];
        }
    }
//Use the median Function to find newest arrays median values.
    float result;
    result = median(d,N2/2) - median(c,N2/2);
    printf("%.1f",result);
    return 0;
}
```
---
# Gaussian Elimination with C
```C
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define mat_elem(a, y, x, n) (a + ((y) * (n) + (x)))

void swap_row(double *a, double *b, int r1, int r2, int n)
{
	double tmp, *p1, *p2;
	int i;

	if (r1 == r2) return;
	for (i = 0; i < n; i++) {
		p1 = mat_elem(a, r1, i, n);
		p2 = mat_elem(a, r2, i, n);
		tmp = *p1, *p1 = *p2, *p2 = tmp;
	}
	tmp = b[r1], b[r1] = b[r2], b[r2] = tmp;
}

void gauss_eliminate(double *a, double *b, double *x, int n)
{
#define A(y, x) (*mat_elem(a, y, x, n))
	int i, j, col, row, max_row,dia;
	double max, tmp;

	for (dia = 0; dia < n; dia++) {
		max_row = dia, max = A(dia, dia);

		for (row = dia + 1; row < n; row++)
			if ((tmp = fabs(A(row, dia))) > max)
				max_row = row, max = tmp;

		swap_row(a, b, dia, max_row, n);

		for (row = dia + 1; row < n; row++) {
			tmp = A(row, dia) / A(dia, dia);
			for (col = dia+1; col < n; col++)
				A(row, col) -= tmp * A(dia, col);
			A(row, dia) = 0;
			b[row] -= tmp * b[dia];
		}
	}
	for (row = n - 1; row >= 0; row--) {
		tmp = b[row];
		for (j = n - 1; j > row; j--)
			tmp -= x[j] * A(row, j);
		x[row] = tmp / A(row, row);
	}
#undef A
}

int main(void)
{
	double a[] = {
		1.00, 0.00, 0.00,  0.00,  0.00, 0.00,
		1.00, 0.63, 0.39,  0.25,  0.16, 0.10,
		1.00, 1.26, 1.58,  1.98,  2.49, 3.13,
		1.00, 1.88, 3.55,  6.70, 12.62, 23.80,
		1.00, 2.51, 6.32, 15.88, 39.90, 100.28,
		1.00, 3.14, 9.87, 31.01, 97.41, 306.02
	};
	double b[] = { -0.01, 0.61, 0.91, 0.99, 0.60, 0.02 };
	double x[6];
	int i;

	gauss_eliminate(a, b, x, 6);

	for (i = 0; i < 6; i++)
		printf("%g\n", x[i]);

	return 0;
}
```
---
# Divide an array into two parts
```C
#include <stdio.h>
#include <stdlib.h>

int main()                             // 1 2 3 4 5 6 7 8 9 10
{
    int i;
    int N,a[50],b[25],c[25];            //0 1 2 3 4 5 6 7 8 9
    scanf("%d",&N);
    for(i=0;i<N;i++){
        scanf("%d",&a[i]);
    }
    if(N%2==1){

        for(i=0;i<N/2;i++){
            b[i]=a[i];
        }
        for(i=0;i<N/2;i++){
            c[i]=a[(N/2)+1+i];
        }
    }
    else{
        for(i=0;i<N/2;i++){
            b[i]=a[i];
        }
        for(i=0;i<N/2;i++){
            c[i]=a[(N/2)+i];
        }
    }
    for(i=0;i<N/2;i++){
        printf("%d ",b[i]);
    }
    printf("\n");
    for(i=0;i<N/2;i++){
        printf("%d ",c[i]);
    }

    return 0;
}
```
---
# Binomial Distribution with C
```C
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

double power(double a, int b){
    int i;
    double result=1.000000;
    if(b==0){
        return 1.0;
    }else{
        for(i=0;i<b;i++){
            result*=a;
        }
        return result;
    }
}
int factorial(int x){
    int i;
    int result=1;
        if(x==0){
            return result;
        }
        else{
            for(i=1;i<=x;i++){
            result*=i;
            }
            return result;
        }
    }
    //If there is 1 child born per birth,
    //what proportion of Russian families with exactly n children will have at least 3 boys?
    //with the given ratio b(oy):g(irl)
double BinoDistr(double b,double g,int n,int t){
    int i;
    double ratio_b=b/(b+g)*1.0,ratio_g=g/(b+g);
        //printf("%lf\n",ratio_b);
        //printf("%lf\n",ratio_g);
    double sum1=1,sum2=1;
    double fact=1;
    double result=0;
        for(i=t;i<=n;i++){
            sum1=power(ratio_b,i);
            sum2=power(ratio_g,n-i);
            fact = (1.0*(factorial(n)))/(1.0*(factorial(i)*factorial(n-i)));
            result+=fact*sum1*sum2;
        }
    return result;
}
int main(){
    int n,t;
    double b,g;
    scanf("%lf %lf %d %d",&b,&g,&n,&t);
    printf("%.3lf",BinoDistr(b,g,n,t));
    return 0;
}
```
---
# SIR Model Covid-19 Infection Rate Simulation
_You can take a look at the model [here](https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology)_
```C
#include <stdio.h>
#include <stdlib.h>
void simulate(double B){
//sn=susceptible at the day
//infn=total infected at that day
//rec1=recoverd at that day.
//B= infectibility rate
//Y= recoveribility rate
//Kodu çalıştırdığımızda bizden B değerini girmemizi istiyor.
//Farklı B değerleri vererek farklı simülasyonlar çalıştırmış oluyoruz.
//Son yazdırılan değerde grafikte çizdirilecek TAU değerini görmüş oluyoruz.

    int i,N=1000;
    double sn,s1=999;
    double infn,inf1=1,Y=0.6;
    double recn,rec1=0;
    double tau;
    double a[101];
    for(i=0;i<100;i++){
            printf("%.2lf    %.2lf   %.2lf   %.4lf \n",s1,inf1,rec1,tau);//to see the results as a chart.

            a[i]=tau;
            tau = 100*(inf1*(1.0))/N;
            sn = s1 -((s1/N)*(B*inf1));
            infn= inf1 + (s1/N)*B*inf1 - inf1*Y;
            recn=rec1 + inf1*Y;

            s1=sn;
            inf1=infn;
            rec1=recn;
        }

        double maxtau=a[0];

        for(i=0;i<100;i++){
            if(a[i]>=maxtau){
                maxtau=a[i];
                if(B<=1){
                  maxtau=0;
                }
            }

        }
    printf("%.3lf\n",maxtau);
}
int main()
{
    double B;
    scanf("%lf",&B);
    float j;

    for(j=1;j<B;j+=0.1){
        simulate(j);
    }


    return 0;
}
```
---
# _The final homework question from 2018-2019 CMPE150 course at Boğaziçi University_
```C
//This code takes an array and gives us the rotated version of 2-D matrix

#include <stdio.h>
#include <string.h>

void read_array(int a[][20],int R,int C){
    int i,j;
    for(i=0;i<R;i++){
        for(j=0;j<C;j++){
            scanf("%d",&a[i][j]);
        }
    }
}
void print_array(int a[][20],int R,int C){
    int i,j;
    for(i=0;i<R;i++){
        for(j=0;j<C;j++){
            printf("%d ",a[i][j]);
        }
        printf("\n");
    }
}
void read_1d(int a[20],int R,int C){
    int i;
    for(i=0;i<R*C;i++){
        scanf("%d",&a[i]);
    }
}
void print_1d(int a[20],int R,int C){
    int i;
    for(i=0;i<R*C;i++){
        printf("%d ",a[i]);
    }
}
int main() {
    
    int a[20],b[20]={0},c[20]={0},R,C,L,i,j,d[20]={0},e[20][20],k=0;
    scanf("%d %d",&R,&C);
    read_1d(a,R,C);
    scanf("%d",&L);
    
    for(i=0;i<L;i++){
        b[i]=a[i];// copy first L entries to a new array b.
    }
    
    for(i=L;i<R*C;i++){
        c[i]=a[i];// And last entries to another array c.
    }

    for(i=0;i<R*C;i++){
        d[i]=c[i+L];//Concatanate c to b in this for and the next one.
    }
    
    for(i=0;i<L;i++){
        d[i+R*C-L]=b[i];
    }
    
    for(i=0;i<R;i++){
		for(j=0;j<C;j++){//Turn 1D array to 2D form.
		e[i][j]=d[k];
		k++;
		}
	}
        print_array(e,R,C);
    
     
    
    return 0;
}
```






