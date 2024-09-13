def binary_search(arr,x,i,j):  
    while i<=j:
        mid=i+(j-i)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binary_search(arr,x,i,mid-1) #using recursion without reccursion we use j=mid-1
        else:
            return binary_search(arr,x,mid+1,j)
    return -1
arr=[20,30,40,50,60,70,80,90]
result=binary_search(arr,80,0,len(arr)-1)
print(result)