import pyautogui as pa
import pyperclip as pe
import time

def paste(txt):
    pe.copy(txt)
    pa.hotkey('ctrl','v')


txt_1 = ['佛山威卡威汽车零部件有限公司','邓达善','龚兆娟','8PU','dashan.deng@foshan-wkw.com','zhaojuan.gong@foshan-wkw.com','4km','16603018850','135 3457 0401',
         ' 广东省佛山市南海区狮山镇红沙工业区惠民路1号 ']
time.sleep(5)
pa.moveTo(381,340)
pa.doubleClick()
pa.hotkey('tab')
for i in txt_1:
    paste(i)
    pa.hotkey('tab')

