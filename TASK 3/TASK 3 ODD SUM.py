def oddsum(a):
     b=0
     for i in a:
          if i%2!=0:
               b=b+i
     return b   
print('sum of odd nos are:',oddsum([3,2,4,6,5,7,8,0,1]))
