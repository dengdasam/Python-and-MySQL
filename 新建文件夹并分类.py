#闂佹彃绉撮幊锟犲触瀹ュ棙鐎�ù鐘猴拷缁辨繈寮�弶璺ㄧ处闁哄倸娲ｅ▎銏″緞閻熸媽瀚欓柛鎺戞�鐞氾拷鏁嶉敓锟�
import os,re,shutil

def Rename():
	i =0
	path='E:\PS教程\PS2019从入门到精通'
	filelist =os.listdir(path)
	for ii in filelist:
		
		print(ii)
		pattern = re.compile('\(.*?\)')
		#pattern = re.compile('P\d')
		newName = re.sub(pattern,"",ii)
		#newName = ii.replace(".mov","")
		oldDir = path+"\\"+ii
		newDir = path+"\\"+ newName
		os.rename(oldDir,newDir)
		
		
def Move():
	
	#ii =[	path="E:\Python閻忓繐褰夌粭鐔兼偟閻犫剝瀵奸悩铏�拷闁规拝鎷烽敓绲�thon閻忓繐褰夌粭鐔兼偟閿熺晫浜告禒瀣��闁告帪鎷烽弫褰掓寠韫囧海鍟婂�鑸电煯缁ㄢ剝瀵煎�锟藉�閻犲�鎷�
	
	for i in range(198,813):
		filelist =os.listdir(path+"\\"+str(i))
		for j in filelist:
			#print(j)
			#jj = j.split('.')[0]
			#if not os.path.exists(path+"\\"+jj):
				#os.makedirs(path+"\\"+jj)
				
			shutil.move(path+"\\"+str(i)+"\\"+j,path)

	
			
		
		
	
	
	
	
	
Rename()
#Move()
		
		