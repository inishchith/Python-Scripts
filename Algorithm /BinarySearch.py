#Binary Search Using Recursion
def binary(arr,start,end,x):
    if end>=start:
        mid=start+(end-start)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binary(arr,start,mid-1,x)
        else:
            return binary(arr,mid+1,end,x)
    else:
        return -1
arr=list(map(int,input().split()))
x=int(input("item to search "))
res=binary(arr,0,len(arr)-1,x)
if res!=-1:
    print("postion of %d in given array is %d"%(x ,res+1))
else:
    print("Not Found")
