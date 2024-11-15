ticket = int(input())
for _ in range(0,ticket):
  n,m = map(int,(input().split()))
  if n>m:
    print(n-m)
  else:
    print(0)
