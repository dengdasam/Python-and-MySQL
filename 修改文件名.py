import os

path = "G:\学习\投资学\(一)投资环境介绍"

filelist =os.listdir(path)
for ii in filelist:
   
    print(ii)
    newName = ii.split('-')[-1]
    oldDir = path+"\\"+ii
    newDir = path+"\\"+ newName
    os.rename(oldDir,newDir)
    

    
