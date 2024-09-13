def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1
arr=[20,45,27,47,55,67,75,88,90]
result=linear_search(arr,67)
print(result)