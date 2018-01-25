#include <bits/stdc++.h>
using namespace std;

int N = 1000000;

//max heap
void heapify(int* arr,int* finish,int root){
	int left = root*2+1,right = root*2+2,size = finish-arr,v = arr[root],i = -1;
	if(left<size && arr[left]>v) {v = arr[left];i = left;}
	if(right<size && arr[right]>v) {v = arr[right];i = right;}
	if(v>arr[root]){
		auto temp = arr[i];arr[i] = arr[root];arr[root] = temp;
		heapify(arr,finish,i);
	}
}

void initialize(int* arr,int* finish,int root = 0){
	if(root>=finish-arr) return ;
	initialize(arr,finish,root*2+1);
	initialize(arr,finish,((root+1)<<1));
	heapify(arr,finish,root);
}

inline void hsort(int* arr,int* finish){
	initialize(arr,finish);
	for(int i=finish-arr-1;i>=0;i--){
		auto temp = arr[0];arr[0] = arr[i];arr[i] = temp;
		heapify(arr,--finish,0);
	}
}

int main(){
	srand(time(NULL));
	int* arr = new int[N], *temp = new int[N];

	for(int i=0;i<N;i++) {arr[i] = rand()%100+1;temp[i]=arr[i];}

	auto start = clock();
	hsort(arr,arr+N);
	auto me = clock();
	sort(temp,temp+N);
	printf("%d %d\n",(clock()-me),(me-start)); 
	
	for (int i = 0; i < N; ++i){if(arr[i]!=temp[i]) cout<<"HELL "<<endl;}	 
	return 0;
}