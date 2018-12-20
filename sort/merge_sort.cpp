/****
归并排序---分治法拆分合并两个已经有序的序列:有小到大
将原有的数组不断的拆分，拆分到不能分割位置，然后开始有小到大合并
步骤：1.拆分  2：合并
****/

#include<iostream>
using namespace std;

//合并---对一个首为start，尾为end的数组按mid划分为前后两个(有序)部分，做合并
void merge(int a[],int start,int end,int mid,int temp[])
{
    int i = start;
    int k = start;
    int j = mid +1;
    while(i<=mid && j<=end){
        if (a[i]<a[j])
            temp[k++] = a[i++];  //一次循环只走一步，两个数组中只有一个后移一步
        else
            temp[k++] = a[j++];
    }
    while(i<=mid)
        temp[k++] = a[i++];
    while(j<=end)
        temp[k++] = a[j++];
    for(int i=start;i<=end;i++)
        a[i] = temp[i];
}


//一次归并过程---将一个数组拆分成两个子数组，再做合并，所以要有待拆分数组的首尾位置即left & right
void mergeSort(int a[],int left,int right,int temp[])
{
    int mid = (left + right)/2;
    //先做拆分，将元素组不断的拆成小的两部分，直到不能拆了为止，也就是每个数组只有一个元素，即这里left = right
    if (left < right){ //还可以继续拆所以继续调用自身来拆数组
        mergeSort(a,left,mid,temp);
        mergeSort(a,mid+1,right,temp);
        //左右归并---在左右归并之前一定要确保拆分到最粒度，如果不要求拆分到最小粒度，而只拆一次，则不需要上面两行代码直接进行左右归并
        merge(a,left,right,mid,temp);
    }
}

int main(){
    int a[] = {2,1,6,4,9,8,3,0,5,7};
    int *temp = new int[10];
    mergeSort(a,0,9,temp);
    for (int i=0;i<10;i++)
        cout << a[i]<<"---";
    return 0;
}
