#include <bits/stdc++.h>
using namespace std;

int N = 8000000;
int* buffer;

template <typename T>
void msort(T* arr,T* finish,T* buffer){
	if(finish-arr<=1) return ;
	T* mid = arr+(finish-arr)/2;
	msort(arr,mid,buffer);
	msort(mid,finish,buffer);

	//merge both sorted sides
	T* l = arr,*r = mid;
	T* temp = buffer,*boo = temp;
	while(true){
		if(*r<*l) {*temp++ = *r++;}
		else {*temp++ = *l++;}
		if(l==mid or r==finish) break;
	}
	while(l!=mid) *temp++ = *l++;
	while(r!=finish) *temp++ = *r++;
	while(arr!=finish) *arr++ = *boo++;
}

int main(){
	srand(time(NULL));
	int* arr = new int[N];
	int* temp = new int[N];
	buffer = new int[N];

	for(int i=0;i<N;i++) {arr[i] = rand()%1000000;temp[i]=arr[i];}

	auto x = clock();
	msort(arr,arr+N,buffer);
	auto y = clock();
	sort(temp,temp+N);
	auto z = clock();
	printf("%d %d\n",(y-x),(z-y)); 

	for (int i = 0; i < N; ++i){if(arr[i]!=temp[i]) cout<<"HELL "<<endl;} 
	return 0;
}

/*
void msort(int* start,int* last){
	if(last-start<=1) return;
	int* mid = start+(last-start)/2;
	msort(start,mid);
	msort(mid,last);

	int *left = start,*right = mid,*put=buffer,*boo=buffer;
	while(left<mid && right<last){
		if(*left<*right) *put++ = *left++;
		else *put++ = *right++;
	}
	while(left<mid) *put++ = *left++;
	while(right<last) *put++ = *right++;
	while(start<last) *start++ = *boo++;

}
*/