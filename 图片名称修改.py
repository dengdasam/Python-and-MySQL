import os

f = os.listdir()


for i in f:
    if i.split(".")[-1] != "py":
        oldName = i
        newName = "在途运单"+str(f.index(i))+".png"
        os.rename(oldName,newName)
    
    