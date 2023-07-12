def reverse_range(arr,begin,end):
    while(end>begin):
        arr[begin],arr[end]=arr[end],arr[begin]
        begin+=1
        end-=1
    return arr
a=list(map(int,input().split()))
b,c = map(int,input().split())
print(reverse_range(a,b,c))


       
