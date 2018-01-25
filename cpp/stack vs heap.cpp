#include <bits/stdc++.h>
using namespace std;

int N = 199900;

void work(){
	int arr[N];
	long long x = 0;
	for (int i = 0; i < N; ++i){arr[i] = i+2;}
	for (int i = 0; i < N; ++i){x=x+arr[i];}
}

void mook(){
	int* arr = new int[N];
	long long x = 0;
	for (int i = 0; i < N; ++i){arr[i] = i+2;}
	for (int i = 0; i < N; ++i){x=x+arr[i];}
}

int main(int argc, char const *argv[])
{
	auto s = clock();
	work();
	auto t = clock();
	mook();
	auto w = clock();
	cout<<(w-t)<<" "<<(t-s)<<endl;
	return 0;
}


