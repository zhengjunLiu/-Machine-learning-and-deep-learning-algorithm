#include<iostream>
#include <math.h>
using namespace std;
void Matrix_Multiplication(double a[] ,double b[],double *c,int m,int n,int p);
void Matrix_multiplied_by_vector(double a[],double b[],double *c,int m,int n);
void Xx(double H[],double b[],double *n,double g[],int M,int N,int In,int Ib);
double qiuafa(double n[],double H[],double d[],int M,int N,int Ind);
bool fanshu(double a[],int M,int N,int Ia);
double qiud(double n[],double H[],double d[],int M,int N,int Ind);
int main()
{
	int i,j,t,N,M;

	double *A,*AT,*b,*n,*d,*H,*g,*x,*afa;
	cout<<"�������������";
	cin>>M;
	cout<<"�������������";
	cin>>N;
	A=(double *)malloc(sizeof(double)*(N*M));//A����
	AT=(double *)malloc(sizeof(double)*(N*M));//Aת��
	d=(double *)malloc(sizeof(double)*(M*10));//d����
	n=(double *)malloc(sizeof(double)*(M*10));//n����
	H=(double *)malloc(sizeof(double)*(N*M));//H����
	g=(double *)malloc(sizeof(double)*(M));//g����
	x=(double *)malloc(sizeof(double)*(M));//x����
	b=(double *)malloc(sizeof(double)*(M));//b����
	afa=(double *)malloc(sizeof(double)*(N));//��������
	for(i=0;i<M;i++)
	{
		x[i*N]=1;//�Զ���d0��
	}

	cout<<"�������A"<<endl;
	for( i=0;i<M;i++)
	{
		for( j=0;j<N;j++)
		{
			 t=(i*N)+j;
			cin>>A[t];
		}
	}//��������
	cout<<"����b����"<<endl;
	for(i=0;i<M;i++)
	{
		cin>>b[i];
	}
	for(i=0;i<M;i++)
	{
		for(j=0;j<N;j++)
		{
			
			AT[j*N+i]=A[i*N+j];
		}
	}//��A ת��
	Matrix_Multiplication(AT,A,H,N,M,N);
	Matrix_multiplied_by_vector(AT,b,g,M,N);
	cout<<"g:"<<g[0]<<" "<<g[1]<<endl;
	cout<<"H:"<<endl;
	for( i=0;i<M;i++)
		{
			for( j=0;j<N;j++)
			{
				 t=(i*N)+j;
				cout<<H[t]<<" ";
			}
			cout<<endl;
		}
	cout<<"d0: ";
	Xx(H,x,n,g,M,N,0,0);//�����һ��n0;
		for(i=0;i<M;i++)
			{
				d[i*N]=-n[i*N];
				cout<<d[i*N]<<" ";
			}
			cout<<endl;

	int w=0;
	double bx;
	while(fanshu(n,M,N,w))
	{
		
		afa[w] =qiuafa(n,H,d,M,N,w);//��ada[w]
	    cout<<"a"<<w<<"; "<<afa[w]<<endl;
	   	w++;
		for(i=0;i<M;i++)
		{
			x[i*N+w]=x[i*N+w-1]+afa[w-1]*d[i*N+w-1];//��x[w]

		}
		cout<<"x"<<w<<": ";
		for(i=0;i<M;i++)
			{
				cout<<x[i*N+w]<<" ";
			}
			cout<<endl;
		Xx(H,x,n,g, M, N,w,w);//��n[w]
		cout<<"n"<<w<<": ";
		for(i=0;i<M;i++)
			{	
				cout<<n[i*N+w]<<" ";
			}
			cout<<endl;

		bx=qiud(n,H,d,M,N,w);//��d[w]
		cout<<"d"<<w<<"; ";
		for(i=0;i<M;i++)
			{
				d[i*N+w]=bx*d[i*N+w-1]-n[i*N+w];
				cout<<d[i*N+w]<<" ";
			}
			cout<<endl;
	}
    free(H);
	free(A);
    free(g);
	free(d);
	free(AT);
	/*
	free(x);
	free(b);
	free(afa);*/
	free(n);
	

}                                                                                                               
void Matrix_Multiplication(double a[] ,double b[],double *c,int m,int n,int p)//m��һ��������У�n��һ�� ������� �ڶ���������У�p�ڶ����������
{
		int i, j, k;  
		for(i = 0; i < m; ++i)  
		{
			for(j = 0; j < p; ++j)  
			{  
				double sum = 0;  
				for(k = 0; k < n; ++k)  
					sum+= a[i*n + k]*b[k*p + j];//
				c[i*p + j] = sum;  
			}  
		}
		 
}
void Matrix_multiplied_by_vector(double H[],double b[],double *c,int m,int n)//�����������
{
	int i, j;
  	for(i = 0; i < m; ++i)  
		{
			double sum=0;
 			for(j = 0; j < n;j++)
			{
				sum+=H[i*n+j]*b[j];
			}
 			c[i]=sum;
                            	
	}
   
}
void Xx(double H[],double b[],double *n,double g[],int M,int N,int In,int Ib)//hx-g,In��n���±�
{
	double *p,*q;
	p=(double *)malloc(sizeof(double)*(M));//g����
	q=(double *)malloc(sizeof(double)*(M));
	for(int i=0;i<M;i++)
	{
		q[i]=b[i*N+Ib];
	}
	Matrix_multiplied_by_vector(H,q,p,M,N);
	for(int i=0;i<M;i++)
	{
		n[i*N+In]=p[i]-g[i];

	}
	free(p);
	free(q);
}
bool fanshu(double a[],int M,int N,int Ia)
{
	double sum;
	double s=0;
	for(int i=0;i<M;i++)
	{
		s=s+a[i*N+Ia]*a[i*N+Ia];
	}
	sum=sqrt(s);
	if(sum>0.00000000000001)
		return true;
	else
		return false;
}
double qiuafa(double n[],double H[],double d[],int M,int N,int Ind)//Ind n ��d ���±�
{
	double *p2,*q2;
	int i;
	p2=(double *)malloc(sizeof(double)*(M));
	q2=(double *)malloc(sizeof(double)*(M));
	for(i=0;i<M;i++)
	{
		p2[i]=d[i*N+Ind];
	}
	Matrix_multiplied_by_vector(H,p2,q2,M,N);
	double sum1=0;
	double sum2=0;
	double sum3;
	 for( i=0;i<M;i++)
			{
				sum1=sum1+d[i*N+Ind]*n[i*N+Ind];
				sum2=sum2+d[i*N+Ind]*q2[i];
		}
    sum3=-(sum1/sum2);
	return sum3;
	free(p2);
	free(q2);

}
double qiud(double n[],double H[],double d[],int M,int N,int Ind)//����dk
{
	double sum1=0,sum2=0,sum3=0;
	double *p3,*q3;
	int i;
	p3=(double *)malloc(sizeof(double)*(M));
	q3=(double *)malloc(sizeof(double)*(M));
	for(i=0;i<M;i++)
	{
		p3[i]=d[i*N+Ind-1];
	}
	Matrix_multiplied_by_vector(H,p3,q3,M,N);
	for(i=0;i<M;i++)
	{
       sum1=sum1+n[i*N+Ind]*q3[i];
	   sum2=sum2+d[i*N+Ind-1]*q3[i];
	}
	sum3=sum1/sum2;
	return sum3;
	free(p3);
	free(q3);
}