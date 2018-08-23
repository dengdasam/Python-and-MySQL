import requests
import re
import pymysql

def getHTMLtext(url):
    
    try:
        r = requests.get(url,timeout =100)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        
        return r.text
    except:
        
        return ""

def getPage(itl,html):
    
    try:
        plt = re.findall(r'"view_price":"[\d.]*"',html)
        nlt = re.findall(r'"raw_title":".*?"',html)
        
        for i in range(len(plt)):
            
            price = eval(plt[i].split(':')[1])
            title = eval(nlt[i].split(':')[1])
            
            itl.append([price,title])
    except:
        
        print("")
       

def printGoods(itl):
    tplt = "{:2}\t{:8}\t{:16}"
    print(tplt.format('序号','价格','商品名称'))
          
    count = 0
    
    conn = pymysql.connect(host = 'localhost',user ='root',password = 'root',db = 'testdb',charset = 'utf8')
    
    cur = conn.cursor()
    
    sqlc = '''  create table coffee(
    id int(11) not null auto_increment primary key,
    name varchar(255) not null,
    price float not null) DEFAULT CHARSET = utf8;'''
    
    try:
        
        A = cur.execute(sqlc)
        conn.commit()
        print('成功1')
    except:
        print('错误1')
        
    for g in itl:
        count = count + 1
        
        b = tplt.format(count,g[0],g[1])
        
        sqla = ''' insert into coffee(name,price)
        values(%s,%s);'''
        
        try:
            
            B = cur.execute(sqla,(g[1],g[0]))
            conn.commit()
            print('成功2')
        except:
            
            print('错误2')
            
    conn.commit()
    cur.close()
    conn.close()
    

    


def main():
    
    goods = '葡萄酒'
    depth = 200
    start_url ='https://s.taobao.com/search?q='+goods
    
    list1 = []
    
    for i in range(depth):
        
        try:
            url = start_url+'&s='+str(i*44)
            html = getHTMLtext(url)
            getPage(list1,html)
            
        except:
            continue
    
    print(printGoods(list1))
    
main()
            
            
        
    
    
    
