#!/usr/bin/env python
# coding: utf-8

# In[7]:


d1={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
d2={10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
d3={2:'twenty',3:'thirty',4:'fourty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
def thousand(s):
    if(s[1:]=='000'):
        print(d1[int(s[0])],'thousand ',end='')
        stop()
    else:
        print(d1[int(s[0])],'thousand ',end='')
        hundred(s[1:])
def hundred(s):
    if(s[1:]=='00'):
        print(d1[int(s[0])],'hundred ',end='')
        stop()
    else:
        print(d1[int(s[0])],'hundred and ',end='')
        last2(s[1:])
def last2(s):
    if(s[0]=='0'):
        print(d1[int(s[1])])
    elif(s[0]=='1'):
        print(d2[int(s[0:])])
    elif(s[1]=='0'):
        print(d3[int(s[0])])
    else:
        print(d3[int(s[0])],d1[int(s[1])])
def stop():
    pass
s=input()
l=len(s)
if(l==4):
    thousand(s)
if(l==3):
    hundred(s)
if(l==2):
    last2(s)
if(l==1):
    print(d1[int(s)])


# In[ ]:




