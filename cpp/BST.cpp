#include <bits/stdc++.h>
using namespace std;

struct Node
{
	Node* parent=NULL,*left=NULL,*right = NULL;
	int value;
	Node(int x,Node* par=NULL) {value = x;parent = par;}
};

void insert(Node* root,int x){
	if(x<root->value){
		if(root->left) insert(root->left,x);
		else root->left = new Node(x,root);
	}
	else{
		if(root->right) insert(root->right,x);
		else root->right = new Node(x,root);
	}
}

void inorder(Node* root){
	if(root==NULL) return;
	inorder(root->left);
	cout<<root->value<<endl;
	inorder(root->right);
}

void pretty_print(Node* root,)

int main(){
	srand(time(NULL));
	int* arr = new int[N];
	for(int i=0;i<N;i++) arr[i] = rand()%100+1;
	Node* tree = new Node(50);
	for(int i=0;i<N;i++) insert(tree,arr[i]);
	inorder(tree);
	return 0;
}