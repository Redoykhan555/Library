#include <bits/stdc++.h>
using namespace std;

struct Vertex
{	
	static int ids;
	int id;
	map<Vertex*,int> mates;
	Vertex(){id=ids++;}
};

int Vertex::ids = 1;

void bfs(Vertex* v){
	queue<Vertex*> q;
	map<Vertex*, int> dist;
	q.push(v);
	dist[v] = 0;

	while(!q.empty()){
		Vertex* cur = q.front();q.pop();
		cout<<cur->id+1<<" "<<dist[cur]<<endl;
		for(auto& m:cur->mates){
			if(dist.count(m.first)>0) 
				dist[m.first] = min(dist[m.first],dist[cur]+1);
			else {
				dist[m.first] = dist[cur]+1;
				q.push(m.first);
			}
		}
	}
}

int main(int argc, char const *argv[])
{
	int N,M,u,v,w;
	cin>>N>>M;
	Vertex* graph = new Vertex[N];
	for(int i=0;i<M;i++){
		cin>>u>>v>>w;
		graph[u-1].mates[graph+v-1] = w;
	}
	bfs(graph);
	return 0;
}

/*
4 6
1 2 5
1 3 3
4 1 6
2 4 7
3 2 4
3 4 5
*/