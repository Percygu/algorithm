#include <iostream>

using namespace std;

int onceQuickSort(int a[],int left,int right)  //一趟排序
{
    int i =left;
    int j =right;
    int num = a[i];
    while(i<j){
    while(a[j]>=num && j>i)
        j--;
    if(i<j){
        a[i] = a[j];
        i++;
    }
    while(a[i]<=num && i<j)
        i++;
    if(i<j){
        a[j] = a[i];
        j--;
    }
   }
    a[i] = num;
    return i;
}

void quickSort(int a[],int left,int right)
{
    if (left <right)
    {
        int i = onceQuickSort(a,left,right); //第一步，找到基准数的位置，左边全部比基准数小，右边全部比基准数大
        quickSort(a,left,i-1);    //同样的方法分治法对左边排序
        quickSort(a,i+1,right);   //同样的方法分治法对右边排序
    }
}

int main()
{
    int a[] = {2,1,5,4,8,7,0,9,3,6};
    quickSort(a,0,9);
    for (int i = 0; i < 10; i++)
        cout<<a[i]<<"---";
    cout<<endl;
    return 0;

}
