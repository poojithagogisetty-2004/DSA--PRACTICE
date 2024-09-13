def ternary_search(arr,i,j,key):
    while i<=j:
        mid1=i+(j-i)//3
        mid2=j-(j-i)//3
        if arr[mid1]==key:
            return mid1
        if arr[mid2]==key:
            return mid2
        elif key<arr[mid1]:
            return ternary_search(arr,i,mid1-1,key)
        elif key >arr[mid2]:
            return ternary_search(arr,mid2+1,j,key)
        else:
            return ternary_search(arr,mid1-1,mid2-1,key)
    return -1
arr=[20,25,47,56,59,63,65,79,82]
result=ternary_search(arr,0,len(arr)-1,63)
print(result)