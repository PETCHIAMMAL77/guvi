k,l=map(int,input().split())
for x in range(k+1,l):
  if(x>1):
    for y in range(2,x):
      if(x%y)==0:
        break
    else:
      print(x,end=" ")
