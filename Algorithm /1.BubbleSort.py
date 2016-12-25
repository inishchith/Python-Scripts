a=list(map(int,input().split()))
x=len(a)
# Traverse through all array elements
for i in range(x):
    #operated x times
    # Last i elements are already in place
    for j in range(0,x-i-1):
        #operated x times
        # traverse the array from 0 to n-i-1
        # Swap if the element found is greater
        # than the next element
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)