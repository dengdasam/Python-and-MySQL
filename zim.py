li_1 = [chr(i) for i in range(65,91)]
li_2 = [chr(i) for i in range(97,123)]
li_3 = li_1+li_2
li_3 = ";".join(li_3)


with open("hello.txt","w+",encoding="utf-8") as hh:
    hh.write(li_3)
    
        
   


    
