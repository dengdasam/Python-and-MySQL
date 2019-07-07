import pyexcel as p
import glob as g

if g.glob('*.xls'):

    for file in g.glob('*.xls'):
        
        print(file)
        
else:
    
    print("目录下无该类型的文件")