from selenium import webdriver
from datetime import datetime
from time import sleep

driver = webdriver.PhantomJS()
begintime=datetime.now()
print("visiting  "+'guancha.cn')
driver.get("http://www.hao123.com")
title = driver.title
print("title is "+title)
print('saving screen ing')
sleep(20)
driver.save_screenshot('guancha.png')
endtime=datetime.now()
stime=endtime-begintime
print('saved! total time(s):'+str(stime.seconds))
