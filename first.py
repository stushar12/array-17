n=int(input("Enter number of elements "))
arr=[]
print("Enter elements :")
for i in range(0,n):
    z=int(input())
    arr.append(z)
k=int(input("Enter a number: "))

low=0
high=n-1
while(low<=high):
    if(arr[high]==k):
        high=high-1
    elif(arr[low]==k ):
        temp=arr[low]
        arr[low]=arr[high]
        arr[high]=temp
        high=high-1
        low=low+1
    else:
        low=low+1


print(f"After transformation array is {arr}")

