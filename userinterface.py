import tkinter as t
def clear():
    global eq
    eq=''
    result.config(text=eq)
def show(t):
    global eq
    eq= eq+t
    result.config(text=eq)
def res():
    global eq
    r=''
    try:
        r=eval(eq)
        eq=''
    except:
        r='Error'
    result.config(text=r)
def back():
    global eq
    if len(eq)>0:
        eq=list(eq)
        eq.pop()
        eq=''.join(eq)
        result.config(text=eq)
        
eq=''
root=t.Tk()
root.title("Basic Calculator")
root.geometry("370x350")
root.resizable(False,False)
root.config(bg='black')

result=t.Label(root,width=100,height=5,text='',font=10)
result.pack()


button = t.Button(root, text="C", width=10,height=2,bg="orange", command=lambda:clear()).place(x=10,y=100)
button = t.Button(root, text="%", width=10,height=2,bg="white", command=lambda:show('%')).place(x=100,y=100)
button = t.Button(root, text="*", width=10,height=2,bg="white", command=lambda:show('*')).place(x=190,y=100)
button = t.Button(root, text="/", width=10,height=2,bg="white", command=lambda:show('/')).place(x=280,y=100)

button = t.Button(root, text="9", width=10,height=2,bg="white", command=lambda:show('9')).place(x=10,y=150)
button = t.Button(root, text="8", width=10,height=2,bg="white", command=lambda:show('8')).place(x=100,y=150)
button = t.Button(root, text="7", width=10,height=2,bg="white", command=lambda:show('7')).place(x=190,y=150)
button = t.Button(root, text="+", width=10,height=2,bg="white", command=lambda:show('+')).place(x=280,y=150)

button = t.Button(root, text="6", width=10,height=2,bg="white", command=lambda:show('6')).place(x=10,y=200)
button = t.Button(root, text="5", width=10,height=2,bg="white", command=lambda:show('5')).place(x=100,y=200)
button = t.Button(root, text="4", width=10,height=2,bg="white", command=lambda:show('4')).place(x=190,y=200)
button = t.Button(root, text="-", width=10,height=2,bg="white", command=lambda:show('-')).place(x=280,y=200)

button = t.Button(root, text="3", width=10,height=2,bg="white", command=lambda:show('3')).place(x=10,y=250)
button = t.Button(root, text="2", width=10,height=2,bg="white", command=lambda:show('2')).place(x=100,y=250)
button = t.Button(root, text="1", width=10,height=2,bg="white", command=lambda:show('1')).place(x=190,y=250)
button = t.Button(root, text="<x", width=10,height=2,bg="white", command=lambda:back()).place(x=280,y=250)

button = t.Button(root, text="0", width=23,height=2,bg="white", command=lambda:show('0')).place(x=10,y=300)
button = t.Button(root, text=".", width=10,height=2,bg="white", command=lambda:show('.')).place(x=190,y=300)
button = t.Button(root, text="=", width=10,height=2,bg="pink", command=lambda:res()).place(x=280,y=300)


root.mainloop()
