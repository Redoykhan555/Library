#include <bits/stdc++.h>
using namespace std;

	struct Node
	{
		bool is_Leaf = false;
		unordered_map<char,Node*> transitions;
	};

	void insert(Node* node,char* str,char* end){
		if(str==end) {node->is_Leaf = true;return ;}
		if (node->transitions[*str]==nullptr) node->transitions[*str] = new Node();
		insert(node->transitions[*str],str+1,end);
	}

	void search(Node* root,char* str,char* end,string so_far=""){
		if(root && root->is_Leaf) cout<<so_far<<endl;
		if(!root or str==end) return;
		so_far.push_back(*str);
		search(root->transitions[*str],str+1,end,so_far); 
	}

	int main(int argc, char const *argv[])
	{
		Node* root = new Node();
		vector<string> prefixes = {"a", "ab", "ba", "aba", "bbb"};
		for(auto& s:prefixes) insert(root,&s[0],&s[0]+s.size());

		string to_search = "abad";
		search(root,&to_search[0],&to_search[0]+to_search.size(),"");
		return 0;
	}