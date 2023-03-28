import pandas as pd

my_list = list(map(int,input("Enter a list of integers: ").split()))
myFinalList = pd.unique(my_list).tolist()
print(myFinalList)
total=0
for ele in range(0, len(myFinalList)):

    total = total + myFinalList[ele]
print("Sum of all elements in given list :" , total)