#include <bits/stdc++.h>
using namespace std;

int N = 10;

void qsort(int* arr,int* finish){
	if(finish-arr<=1) return ;
	int *i=arr,temp;
	auto pivot = *(finish-1);
	if(finish-arr==N){
		for(int q=0;q<N;q++) cout<<arr[q]<<endl;
		cout<<endl;
	}
	for(int* j=arr;j<finish-1;j++){
		if(*j<=pivot) {temp = *j;*j=*i;*i=temp;i++;}
		j++;
	}
	cout<<endl;
	if(finish-arr==N){
		for(int q=0;q<N;q++) cout<<arr[q]<<endl;
	}
	temp = *(finish-1);*(finish-1)=*i;*i=temp;
	qsort(arr,i);
	qsort(i+1,finish);
}
//5,6,0,3,9,1,4,9
int main(int argc,char** argv){
	srand(time(NULL));
	if(argc==2) N = atoi(argv[1]);

	int* arr = new int[N], *temp = new int[N];
	for(int i=0;i<N;i++) {arr[i] = rand()%100+1;temp[i]=arr[i];}
	
	auto start = clock();
	qsort(arr,arr+N);

	auto me = clock();
	sort(temp,temp+N);
	printf("%d %d\n",(clock()-me),(me-start)); 
	
	for (int i = 0; i < N; ++i){if(arr[i]!=temp[i]) cout<<arr[i]<<" "<<temp[i]<<endl;}	 
	return 0;
}