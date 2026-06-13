def reverse(arr,a,b):
    if a>=b:
        return
    arr[a],arr[b]=arr[b],arr[a]
    return reverse(arr,a+1,b-1)


arr=[1,2,3,4,5]
reverse(arr,1,3)
print(arr)