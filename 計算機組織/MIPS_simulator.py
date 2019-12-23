import math
op = ""
num = ""
Op = []
#-------------
Ins = []
Ins_num = [0,0,0]
#IF = 0
#ID = 0
#EX	= 0					
#MEM = 0					
#WB = 0				
cycle = 0

register = [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
word     = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

R_format_pipe = '110000010'
lw_pipe = '000101011'
sw_pipe = 'X0010010X'
beq_pipe = 'X0101000X'
def lw(x,y,z):
    register[x]=word[(int)(register[z]+y/4)]
def sw(x,y,z):
    word[int(y/4+register[z])]=register[x]
def add(x,y,z):
    register[x]=register[y]+register[z]
def sub(x,y,z):
    register[x]=register[y]-register[z]
#def beq(x,y,z):
f = open('memory1.txt','r')
op_flag = 0
num_flag = 0
for char in f.read():
    if (op_flag) == 0:
        if(char != ' '):
            op=op+char
        if(char == ' '):
            #print(op)
            Op.append(op)
            op_flag=1
    if(ord(char)==45):
        num=num+char
    if(ord(char)>=48 and ord(char)<=57):
        num=num+char
    if(ord(char)!=45):
        if(ord(char)<48 or ord(char)>57):
            #print(num+' ',end='')
            Op.append(num)
            num=''
    if(char == '\n'):
        op=''
        op_flag = 0
op_count=0  
for i in range(len(Op)):
    if(Op[i]!=''):
        Ins.append(Op[i])
for i in range(len(Ins)):
    if(i%4==0):
        if(Ins[i]=='lw'):
            print('lw',end=' ') 
            print(Ins[i+1],end=' ')
            print(Ins[i+2],end=' ')
            print(Ins[i+3])
            str_=Ins[i+1]
            if(str_[0]=='-'):
                #print(str_[1:len(str_)])
                Ins_num[0]=int(str_[1:len(str_)])*(-1)
            elif(str_[0]!='-'):
                Ins_num[0]=int(str_)
            #print(Ins_num[0])
            str_=Ins[i+2]
            if(str_[0]=='-'):
                #print(str_[1:len(str_)])
                Ins_num[1]=int(str_[1:len(str_)])*(-1)
            elif(str_[0]!='-'):
                Ins_num[1]=int(str_)
            #print(Ins_num[0])

            str_=Ins[i+3]
            if(str_[0]=='-'):
                #print(str_[1:len(str_)])
                Ins_num[2]=int(str_[1:len(str_)])*(-1)
            elif(str_[0]!='-'):
                Ins_num[2]=int(str_)
            #print(Ins_num[0])
            lw(Ins_num[0],Ins_num[1],Ins_num[2])
        if(Ins[i]=='sw'):
            print('sw',end=' ')
            print(Ins[i+1],end=' ')
            print(Ins[i+2],end=' ')
            print(Ins[i+3])
            str_=Ins[i+1]
            if(str_[0]=='-'):
                #print(str_[1:len(str_)])
                Ins_num[0]=int(str_[1:len(str_)])*(-1)
            elif(str_[0]!='-'):
                Ins_num[0]=int(str_)
            #print(Ins_num[0])
            str_=Ins[i+2]
            if(str_[0]=='-'):
                #print(str_[1:len(str_)])
                Ins_num[1]=int(str_[1:len(str_)])*(-1)
            elif(str_[0]!='-'):
                Ins_num[1]=int(str_)
            #print(Ins_num[0])
            str_=Ins[i+3]
            if(str_[0]=='-'):
                #print(str_[1:len(str_)])
                Ins_num[2]=int(str_[1:len(str_)])*(-1)
            elif(str_[0]!='-'):
                Ins_num[2]=int(str_)
            #print(Ins_num[0])
            sw(Ins_num[0],Ins_num[1],Ins_num[2])
        if(Ins[i]=='add'):
            print('add',end=' ')
            print(Ins[i+1],end=' ')
            print(Ins[i+2],end=' ')
            print(Ins[i+3])
            str_=Ins[i+1]
            if(str_[0]=='-'):
                #print(str_[1:len(str_)])
                Ins_num[0]=int(str_[1:len(str_)])*(-1)
            elif(str_[0]!='-'):
                Ins_num[0]=int(str_)
            #print(Ins_num[0])

            str_=Ins[i+2]
            if(str_[0]=='-'):
                #print(str_[1:len(str_)])
                Ins_num[1]=int(str_[1:len(str_)])*(-1)
            elif(str_[0]!='-'):
                Ins_num[1]=int(str_)
            #print(Ins_num[0])
            str_=Ins[i+3]
            if(str_[0]=='-'):
                #print(str_[1:len(str_)])
                Ins_num[2]=int(str_[1:len(str_)])*(-1)
            elif(str_[0]!='-'):
                Ins_num[2]=int(str_)
            #print(Ins_num[0])
            add(Ins_num[0],Ins_num[1],Ins_num[2])
        if(Ins[i]=='sub'):
            print('sub',end=' ')
            print(Ins[i+1],end=' ')
            print(Ins[i+2],end=' ')
            print(Ins[i+3])
            str_=Ins[i+1]
            if(str_[0]=='-'):
                #print(str_[1:len(str_)])
                Ins_num[0]=int(str_[1:len(str_)])*(-1)
            elif(str_[0]!='-'):
                Ins_num[0]=int(str_)
            #print(Ins_num[0])
            str_=Ins[i+2]
            if(str_[0]=='-'):
                #print(str_[1:len(str_)])
                Ins_num[1]=int(str_[1:len(str_)])*(-1)
            elif(str_[0]!='-'):
                Ins_num[1]=int(str_)
            #print(Ins_num[0])
            str_=Ins[i+3]
            if(str_[0]=='-'):
                #print(str_[1:len(str_)])
                Ins_num[2]=int(str_[1:len(str_)])*(-1)
            elif(str_[0]!='-'):
                Ins_num[2]=int(str_)
            #print(Ins_num[0])
            sub(Ins_num[0],Ins_num[1],Ins_num[2])
        if(Ins[i]=='beq'):
            print('beq',end=' ')
            print(Ins[i+1],end=' ')
            print(Ins[i+2],end=' ')
            print(Ins[i+3])
            str_=Ins[i+1]
            if(str_[0]=='-'):
                #print(str_[1:len(str_)])
                Ins_num[0]=int(str_[1:len(str_)])*(-1)
            elif(str_[0]!='-'):
                Ins_num[0]=int(str_)
            #print(Ins_num[0])
            str_=Ins[i+2]
            if(str_[0]=='-'):
                #print(str_[1:len(str_)])
                Ins_num[1]=int(str_[1:len(str_)])*(-1)
            elif(str_[0]!='-'):
                Ins_num[1]=int(str_)
            #print(Ins_num[0])
            str_=Ins[i+3]
            if(str_[0]=='-'):
                #print(str_[1:len(str_)])
                Ins_num[2]=int(str_[1:len(str_)])*(-1)
            elif(str_[0]!='-'):
                Ins_num[2]=int(str_)
            #print(Ins_num[0])
            #beq(Ins_num[0],Ins_num[1],Ins_num[2])
        print(Ins_num)
print(register)
print(word)
