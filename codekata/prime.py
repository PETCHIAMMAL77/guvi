ee=eval(input())
if(ee>1):
  for i in range(2,ee):
    if(ee%i==0):
      print("no")
      break
  else:
    print("yes")
else:
  print("no")
