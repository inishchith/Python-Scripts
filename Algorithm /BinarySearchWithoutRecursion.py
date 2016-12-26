#binarySearch without recursion
import timeit
def binary(arr,start,end,item):
    time1=timeit.default_timer()
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==item:
            time2 = timeit.default_timer()
            print("Time taken : ", time2 - time1)
            return mid
        elif arr[mid]>item:
            end=mid-1
        else:
            start=mid+1
    time2=timeit.default_timer()
    print("Time taken : ", time2-time1)
    return -1
arr=list(map(int,input("Enter Array Elements: ").split()))
item =int(input("Enter Item to be searched: "))
result=binary(arr,0,len(arr)-1,item)
if result!=-1:
    print("item found at ",result+1)
else:
    print("Not Found")
