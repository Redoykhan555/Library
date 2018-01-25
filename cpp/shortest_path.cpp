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

void dijkstra(Vertex* v){
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
	auto hal = [](pair<int,int> p,pair<int,int> q){
		return p.first<q.first;
	};
	multiset<pair<int,int> > que(hal);
	que.insert(make_pair(6,5));
	que.insert(make_pair(62,511));
	que.insert(make_pair(8,90));

	//auto it = lower_bound(que.begin(),que.end(),9);
	//auto iit = upper_bound(que.begin(),que.end(),9);
	//que.erase(it,iit);
	for(auto& x:que) cout<<x.first<<endl;

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