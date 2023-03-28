ls1=[]
for i in range (4):
  n =int (input ("Enter a number:"))
  ls1.append(n)
print (ls1)
min = ls1[0]
 
#finding smallest number
for i in range (len (ls1)):
  if ls1[i] < min:
    min = ls1[i]
print ("The smallest element is ", min)
