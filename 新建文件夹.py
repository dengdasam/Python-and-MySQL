import os,sys

def creatdirs():

    
    path = ['F11','SPV','W66','W77','X55-Q2','Golf-A7','Golf-BEV','X55-BEV','T-ROC','T-ROC-Rline']
    
    tree = ['BOM','包装作业指导书','包装器具资料','包装作业指导书扫描版','产品图片','产品尺寸资料']
    for i in path:
        if not os.path.exists(i):
            os.makedirs(i,493)
                       
    for i in path:
        for j in tree:
            if not os.path.exists(r"{0}/{1}".format(i,j)):
                os.makedirs(r"{0}/{1}".format(i,j),493)  

str1 = input("现在将新建包装方案目录文件夹；请输入Y(确认)/N(退出)： ")
str1 = str1.upper()
           
if str1 == "Y":
    creatdirs()
else:
    exit()
    

print("Done")
input()

