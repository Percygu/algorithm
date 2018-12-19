/****
直接插入排序
在已有的已经排好序的序列里依次插入待排序的数字
原地排序，不新增新的数组
 ***/
#include<iostream>
using namespace std;
void insert_sort(int a[],int n)
{
    for (int i=1;i<n;i++)   //从原数组的第二个数开始依次把后面的数往前面插入
    {
        int j = i-1;
        int k = a[i];  //因为是在原数组上排序，
        while(a[j]>=k && j>=0){
            a[j+1] = a[j];
            j--;
        }
        a[j+1] = k;
    }

}

int main()
{
    int num[] = {3,4,1,8,6,5,0,2,7,9};

    insert_sort(num,10);

    for(int i=0;i<10;i++)
    {
        cout<<num[i]<<endl;
    }
    return 0;
}
