/*****
迪杰斯塔拉算法求最短路径
用二维数组存储图
****/
#include <iostream>
#include <fstream>
#include <string>

using namespace std;
#define MaxSize 10
#define costMax 10000

template<class T>
//定义图结构---邻接矩阵
struct Graph
{
    int vertexNum;  //定点数量
    int arcNum;     //边数量
    T vertex[MaxSize];  //定义定点数组，目前有MaxSize个定点，定点的表示类型可以是任意类型，用模板类表示
    int arc[MaxSize][MaxSize]; //二维数组表示边，比如arc[1][2]表示第1个定点到第2个定点的距离，所以类型是整型
};

//dijstra算法----定点类型为string类型，求第v个定点到图中各点的最短路径
void dijstra(Graph<string> G,int v)
{
    int dist[MaxSize];  ///定义dist数组，用于存放各个点到v定点的路径距离，用于更新，直至最短距离，则将该点加入到s集合
    string path[MaxSize]; //
    int s[MaxSize]; //保存已经找到的最短路径的集合
    bool find[MaxSize]; //判断定点是否已经加入到s集合中

    //初始化图----用相邻距离初始化各个边的距离，保存到dist数组中
    for (int i = 0;i < G.vertexNum;i++){
        find[i] = false;  //各个定点到v的距离还没找到
        dist[i] = G.arc[v][i];
        if(dist[i]!=costMax)
            path[i] = G.vertex[v] + G.vertex[i];
        else
            path[i] = " ";
    }

    s[0] = v;
    find[v] = true;
    int num = 1;  //s集合中已经加入了一个定点v

    while(num < G.vertexNum){  //循环将剩余顶点添加到s集合中，直至s集合中包含所有顶点
        int mindist = costMax;
        int k = 0;
        //在dist数组中查找最小值元素
        for (int i = 0;i<G.vertexNum;i++)
        {
            if (!find[i]&&dist[i]<mindist){
                mindist = dist[i];
                k = i;
            }
        }
        cout<<path[k]<<"----"<<dist[k]<<endl;
        s[num++] = k;
        find[k] = true;

        //更新dist数组和path数组
        for(int i=0;i<G.vertexNum;i++)
        {
            if(!find[i]&&dist[i]>dist[k]+G.arc[k][i]){
                dist[i] = dist[k] + G.arc[k][i];
                path[i] = path[k] + G.vertex[i];
            }
        }
    }
}


int main(){
    //构建图
    Graph<string> G;
    string v[] = {"v0","v1","v2","v3","v4"};
    ifstream in("input.txt");
    in >> G.vertexNum >> G.arcNum;  //将txt文件中前两个数字读出赋值给G的顶点数和边数
    for (int i=0;i<G.vertexNum;i++)
    {
        G.vertex[i] = v[i];
    }

    //初始化图G的各个边的权值为costMax
    for (int i=0;i<G.vertexNum;i++)
    {
        for (int j=0;j<G.vertexNum;j++)
        {
            G.arc[i][j] = costMax;
        }
    }

    //按照txt文件给对应的边赋值
    for(int i=0;i<G.arcNum;i++)
    {
        int sourceV,sinkV,dist;
        in>>sourceV>>sinkV>>dist;
        G.arc[sourceV][sinkV] = dist;
    }

    dijstra(G,0);
    return 0;
}
