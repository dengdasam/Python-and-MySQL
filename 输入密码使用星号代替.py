import msvcrt,sys,os

print('password:',end="",flush = True)

li = []

while 1:
    ch = msvcrt.getch()
    if ch == b'\r':
        msvcrt.putch(b'\n')
        print('密码是： %s'%b''.join(li).decode())
    elif ch == b'\x08':
        if li:
            li.pop()
            msvcrt.puth(b'\b')
            msvcrt.puth(b'')
            msvcrt.puth(b'\b')
    elif ch == b'\x1b':
        break
    else:
        li.append(ch)
        msvcrt.putch(b'*')
        
os.system("pause")
