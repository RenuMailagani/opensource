N,X,Y=map(int,input().strip().split())
p=False
for i in range(N+1):
    t_s=i*X+(N-i)*0
    if t_s==Y:
        p=True
        break
if p:
    print("YES")
else:
    print("NO")
