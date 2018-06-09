#include <iostream>
#define N 2000
using namespace std;

int mat[N][N];
int sorted[N];
bool vis[N];
int n,m,T;

void tsort(int v){
	vis[v] = true;
	for (int i = 0; i < n; ++i)
	{
		if(mat[v][i] && vis[i]==false) tsort(i);
	}
	sorted[T--] = v;
}

int main(int argc, char const *argv[])
{
	cin>>n>>m;
	T = n-1;
	int u,v,w;
	for (int i = 0; i < m; ++i)
	{
		cin>>u>>v;
		mat[u-1][v-1] = 1;
	}

	for (int i = 0; i < n; ++i)
	 {
	 	if (vis[i]==false) tsort(i);
	 }
	 for (int i = 0; i < n; ++i)
	 {
	 	cout<<sorted[i]<<endl;
	 }
	return 0;
}

