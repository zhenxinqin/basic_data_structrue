
#include <iostream>
#include <stack>
#include <queue>
using namespace std; 
int n,i,j;
int res;
stack <int> s;
queue <int> in,out;
void clear(stack <int> &s){

	while(!s.empty())
	s.pop();
}
void clear(queue <int> &s){

	while(!s.empty())
	s.pop();
}
void print(queue <int> i){

	while(!i.empty()){

		cout<<i.front();
		i.pop();
		}
cout<<endl;
}

void dostack(queue <int> in,stack <int> s,queue <int> out){

if(in.empty())//输入队列空
	{
		if(s.empty())//堆栈空
		{
		res++;
		print(out);
		}
		else//堆栈不空
		{
		out.push(s.top());//堆栈-->输出队列
		s.pop();
		dostack(in,s,out);
		}
	}
else//输入队列不空
	{
		if(!s.empty())//堆栈不空
		{
			stack <int> ts;
			queue <int> tin,tout;
			tin=in;
			ts=s;
			tout=out;

			tout.push(ts.top());//堆栈-->输出队列
			ts.pop();
			dostack(tin,ts,tout);
		}
		
		s.push(in.front());//输入队列-->堆栈
		in.pop();
		dostack(in,s,out);
	}
}

//主函数
int main(){
printf("input a number\n");
while(cin>>n){
	res=0;
	clear(in);
	clear(out);
	clear(s);
	for(i=n;i>=1;i--)
		in.push(i);
	dostack(in,s,out);
	cout<<"total:"<<res<<endl;
}
return 0;
}

