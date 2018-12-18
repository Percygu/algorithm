/****三角形求路径最大值
 7
 3   8
 8   1   0
 2   7   4   4
 4   5   2   6   5
 如以上三角形，从其中一个数走到底边，每一步只能往下走或向右下方走，比如顶点7只能到3或者8，求所经过的路径的最大和
****/


/***
简单的递归思路
****/
#include<iostream>

#define MAXNUM 100

using namespace std;

int triangle[MAXNUM][MAXNUM];

int maxPath[MAXNUM][MAXNUM];

int maxSum(int i,int j,int n) //n表示三角形的行数，第i行第j列的数到底边的最大路径和
{
    if(i==n){
        return triangle[i][j];
    }else if(i>n){
        return 0;
    }else{
        int x = maxSum(i+1,j,n);
        int y = maxSum(i+1,j+1,n);
        return max(x,y)+triangle[i][j];
    }
}


/***
    简单的递归存在大量的重复计算，在递归的基础上将之前计算过的值保存起来----记忆型递归
****/
//需要定义一个数组用来存储已经计算过的子最大路径和

int memarySum(int i ,int j,int n)
{
    //判断这个点的最长路径与没有被计算过，若没有被计算过则计算
    if (maxPath[i][j] != -1){  //已经被计算过
        return maxPath[i][j];
    }
    if (n >= MAXNUM){
        cout<<"输入的行数超过最大值";
        return 0;
    }
    if (i==n){
        return triangle[i][j];
    }else{
        int x = memarySum(i+1,j,n);
        int y = memarySum(i+1,j+1,n);
        return max(x,y)+triangle[i][j];
    }
}

/***逆向思维-----动态规划
由于总要走到最下面一层边才结束，所以逆向递推
*****
7                         30
3 8                       23 21
8 1 0                     20 13 10
2 7 4 4                   7  12 10 10
4 5 2 6 5                 4  5  6  2  5
如右图所示，最后一排的最长路径就是各个节点自身，倒数第二排的最短路径，比如第一个点，2可以到最后一排的4或者5，到5的距离更大，则在此位置上
保存2+5=7
****/
int getDPsum(int i,int j,int n)
{
    if (i == n)
        return triangle[i][j];
    for(int k=n-1;k>=i;k--)
    {
        for(int l=1;l<=k;l++)
        {
                int x = triangle[k][l]+triangle[k+1][l];
                int y = triangle[k][l]+triangle[k+1][l+1];
                triangle[k][l] = max(x,y);
                cout<<"triangle["<<k<<"]["<<l<<"]="<<triangle[k][l]<<endl;

        }
    }
    return triangle[i][j];
}




int main()
{
    int n;
    cout<<"三角形的行数是：";
    cin>>n;
    if(n>=MAXNUM){
        cout<<"输入的行数超过最大值";
        return 0;
    }
    for(int i=1;i<=n;i++)
        for(int j=1;j<=i;j++)
        {
            maxPath[i][j] = -1;       //初始化记录子最长路径的数组值为-
            cin>>triangle[i][j];
        }
    int pathsum = maxSum(1,1,n);
    int memarysum = memarySum(1,1,n);
    int dpSum = getDPsum(1,1,n);
    cout<<"简单递归最大路径和是："<<pathsum<<endl;
    cout<<"记忆递归最大路径和是："<<memarysum<<endl;
    cout<<"动态递推最大路径和是："<<dpSum<<endl;
    return 0;
}
