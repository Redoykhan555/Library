#include <stdio.h>
#include <time.h> 
#include <stdlib.h> 
#include <algorithm>   
using namespace std;

int N = 10;

void disp(int* arr){
	for (int i = 0; i < N; ++i)
	{
		printf("%d\n", arr[i]);
	}
	printf("\n");
}

template <typename T>
void swapp(T* a,T* b){
	printf("swapping %d %d\n",*a,*b);
	swap(a,b);
}

template <typename T>
void partition(T* arr,T* finish,T v){
	T* left = arr,*right = finish-1;
	for(auto i = arr;i<finish;){
		printf("index :%d\n",*i);
		if(*i<v){
			while(*left<v && left<i){left++;}
			if(i==left) i++;
			else swap(left,i);
		}
		else if(*i>v){
			while(*right>v && right>i){right++;}
			if(i==right) i++;
			else swap(right,i);
		}
		else i++;
		disp(arr);
	}
}



int main(int argc, char const *argv[])
{

	srand(time(NULL));
	int* arr = new int[N], *temp = new int[N];

	for(int i=0;i<N;i++) {arr[i] = rand()%10+1;temp[i]=arr[i];}
	
	printf("%d\n\n", arr[0]);


	partition(arr,arr+N,6);
	
	return 0;
}
