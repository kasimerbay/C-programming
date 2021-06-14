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






