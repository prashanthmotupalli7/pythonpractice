count=9
count1=91
for i in range(5):
    for j in range(5):
      if i%2==0:
          count=count+1
          print(count,end=" ")
      else:
        count1=count1-1
        print(count1,end=" ")
    print()