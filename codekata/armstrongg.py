c,d=map(int,input().split())
for i in range(c+1,d):
  x=0
  y=i
  while(y>0):
    z=y%10
    y=y//10
    e=z**3
    x=x+e
  if(i==x):
    print(x,end=' ')
