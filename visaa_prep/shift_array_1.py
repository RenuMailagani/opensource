N=int(input().strip())
a=list(map(int,input().strip().split()))
if N>0:
    f_element=a[0]
    for i in range(1,N):
        a[i-1]=a[i]
    a[N-1]=f_element
print(" ".join(map(str,a)))
