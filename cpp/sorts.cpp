#include <bits/stdc++.h>
using namespace std;

int N = 4000000;//00000;
int* buffer;

void msort(int* arr,int* finish){
	if(finish-arr<=1) return ;
	int* mid = arr+(finish-arr)/2;
	msort(arr,mid);
	msort(mid,finish);

	//merge both sorted sides
	int* l = arr,*r = mid;
	int* temp = buffer,*boo = temp;
	while(true){
		if(*r<*l) {*temp++ = *r++;}
		else {*temp++ = *l++;}
		if(l==mid or r==finish) break;
	}
	while(l!=mid) *temp++ = *l++;
	while(r!=finish) *temp++ = *r++;
	while(arr!=finish) *arr++ = *boo++;
}

void qsort(int* arr,int start=0,int finish=N-1){
	if(start>=finish) return ;
	int i=start+1,j = finish,temp;
	auto pivot = arr[start];
	while(i!=j){
		while (arr[j]>=pivot && j>i) --j;
		while (arr[i]<pivot && i<j) ++i;
		if(i==j) break;
		temp=arr[i];arr[i]=arr[j];arr[j]=temp; //swap big guy to right side
	}
	if(arr[i]>=arr[start]) --i;

	temp = arr[start];arr[start]=arr[i];arr[i]=temp; //swap pivot
	qsort(arr,start,i-1);
	qsort(arr,i+1,finish);
}

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
	int* arr = new int[N], *temp = new int[N],*boo = new int[N];
	buffer = new int[N];

	for(int i=0;i<N;i++) {arr[i] = rand()%1000+1;temp[i]=arr[i];boo[i] = arr[i];}

	auto t1 = clock();
	msort(arr,arr+N);
	auto t2 = clock();
	hsort(temp,temp+N);
	auto t3 = clock();
	qsort(boo);
	auto t4 = clock();
	printf("m:%d h:%d q:%d\n",t2-t1,t3-t2,t4-t3); 
	
	//for (int i = 0; i < N; ++i){if(arr[i]!=temp[i]) cout<<"HELL "<<endl;}	 
	return 0;
}