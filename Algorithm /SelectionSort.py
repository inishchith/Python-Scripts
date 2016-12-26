a=list(map(int,input().split()))
x=len(a)
# Traverse through all array elements
for i in range(x):
    min_=i
    # Find the minimum element in remaining unsorted array
    for j in range(i+1,x):
        if a[min_]>a[j]:
            min_=j
    # Swap the found minimum element with the first element
    a[i],a[min_]=a[min_],a[i]
print(a)
