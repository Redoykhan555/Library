#include <bits/stdc++.h>
using namespace std;

int N = 101;

template <typename T>
T* lower(T* start,T* end,T v){
	while(true){
		T* m = start + (end-start)/2;
		if(m==start) return end;
		if(*m<v) start = m;
		else end = m;
	}
}

int main(){
	srand(time(NULL));
	int* arr = new int[N];
	for(int i=0;i<N;i++) {arr[i] = rand()%100+1;}
	cout<<endl;

	sort(arr,arr+N);

	int* x = lower_bound(arr,arr+N,15);
	int* y = lower(arr,arr+N,15);
	cout<<*x<<" "<<*y<<endl;
	return 0;
}



