#include <bits/stdc++.h>
using namespace std;
using namespace std::placeholders; 

int boo(int x,int (*f) (int)){
	return f(x);
}

int fool(int i,int x){
	return i+x;
}

int main(int argc, char const *argv[])
{
	auto bal = bind(fool,10,_1);
	cout<<boo(4,bal)<<endl;
	return 0;
}
