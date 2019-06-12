x,y=input().split()
x=int(x)
y=int(y)
s=0
array=[int(a) for a in input().split()]
for i in range (0,y):
  s=s+array[i]
print(s)
