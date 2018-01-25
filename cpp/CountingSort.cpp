#include <bits/stdc++.h>
using namespace std;

int N = 10;

void csort(int* arr,int* end,int(*foo)(int)){
	int n=end-arr;
	int k = *max_element(arr,end);
	vector<int> bb(n,0),cc(k+1,0);

	for(int* i=arr;i<end;i++) cc[foo(*i)]++;

	for(int i=1;i<k+1;i++) cc[i]=cc[i]+cc[i-1];

	for(int j=n-1;j>-1;j--){
		bb[cc[arr[j]]-1]=arr[j];
		cc[arr[j]]--;
	}

	for(int i=0;i<n;i++) arr[i] = bb[i];
}

int fool(int i,int x){
	int r;
	while(i--) {r = x%10;x-=r;x/10;}
	return r;
}

void rsort(int* start,int* end){
	using namespace std::placeholders; 
	int m = *max_element(start,end); 
	int steps = m==0?1:0,x=1;
	while(x<=m) {steps++;x*=10;}

	for(int i=1;i<=steps;i++) {
		auto lambu = bind(fool,i,_1);
		csort(start,end,lambu);
	}
}

int main(){
	srand(time(NULL));
	int* arr = new int[N];
	int* temp = new int[N];

	for(int i=0;i<N;i++) {arr[i] = rand()%101;temp[i]=arr[i];}

	/*auto x = clock();
	csort(arr,arr+N,[](int x){return x;});
	auto y = clock();
	sort(temp,temp+N);
	auto z = clock();
	printf("%d %d\n",(y-x),(z-y)); 

	for (int i = 0; i < N; ++i){if(arr[i]!=temp[i]) cout<<"HELL "<<endl;}
	rsort(arr,arr+N);*/

	return 0;
}
