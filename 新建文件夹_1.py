import os,sys

def creatdirs():

    
    #path = ['F11','SPV','W66','W77','X55-Q2','Golf-A7','Golf-BEV','X55-BEV','T-ROC','T-ROC-Rline']
    
    #tree = ['BOM','包装作业指导书','包装器具资料','包装作业指导书扫描版','产品图片','产品尺寸资料']
    tree_1 = ['5GE.863.045B',
            '5GE.863.046B',
            '5GE.863.241D',
            '5G1.863.487C',
            '5G1.863.488B',
            '5G1.864.263AS',
            '5G1.864.263AT',
            '5GE.864.761B',
            '5GE.861.513B',
            '5G0.035.640',
            '5GE.864.298B',
            '5G0.863.135C',
            '5GE.863.328',
            '5GE.864.123',
            '5G1.864.148',
            '5GE.863.179',
            ]
    #for i in path:
        #if not os.path.exists(i):
            #os.makedirs(i,493)
                       
    #for i in path:
        #for j in tree:
            #if not os.path.exists(r"{0}/{1}".format(i,j)):
                #os.makedirs(r"{0}/{1}".format(i,j),493)
                
    for j in tree_1:
        #if not os.path.exists(r"{0}/{1}".format(i,j)):
        os.makedirs(r"{0}".format(j),493)     

str1 = input("现在将新建包装方案目录文件夹；请输入Y(确认)/N(退出)： ")
str1 = str1.upper()
           
if str1 == "Y":
    creatdirs()
else:
    exit()
    

print("Done")
input()

