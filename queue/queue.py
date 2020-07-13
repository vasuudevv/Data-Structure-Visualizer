from tkinter import*
from tkinter import ttk
import random
from tkinter import messagebox

root =Tk()
root.title("QUEUE")
root.maxsize(1000,1000)            #opening window
root.config(bg="black")


#frame base layout
ui_frame= Frame(root, width=600, height=200,bg="grey")
ui_frame.grid(row=0,column=0,padx=10,pady=5)
#canvas
canvas= Canvas(root, width=900, height= 380, bg="black")
canvas.grid(row=1, column=0,padx=10, pady=5)

#variables
x=40
y=160
xf=40
yf=160
list1=[]
x0=40
y0=100
x1=100
y1=160
listrear=[]
listfront=[]
listele=[]
pointer=0

#functions
popped=canvas.create_text(700,300, text="The dequeued element was: ", fill="white")

def enque():
    global x
    global nn
    global list1
    global x0
    global x1
    global y1
    global y0
    global listrear
    global txtrear
    global listfront
    global txtfront
    global listele
    global pointer


    listele.append(int(eleEntry.get()))
    element=eleEntry.get()
    length=len(listrear)

    if len(listele)<=14:
        canvas.create_rectangle(x0,y0,x1,y1 ,fill="black",outline="white")   #create the array box
        ele=canvas.create_text(x+30,y+20, text=pointer,font=("arial", 12), fill="lightgreen")


        x0+=60
        x1+=60
        pointer+=1



        txt=canvas.create_text(x+30,y-30, text=element,font=("arial", 12), fill="orange")      #push the element
        txtrear=canvas.create_text(x+30,y-70, text="REAR", fill="red")        #display top tag for the element on  the top
        if pointer==1:
            txtfront=canvas.create_text(xf+30,yf-90, text="FRONT", fill="red")

            listfront.append(txtfront)
        listrear.append(txtrear)
        if length>1:
            canvas.delete(listrear[length-1])
        if length==1:
            canvas.delete(listrear[0])
        list1.append(txt)
        # if len(list1)>0:
        x+=60
    else:
        response=messagebox.showwarning("Warning","Array limit: 13")
    print(len(listele))
    # print(listrear)
    # print("***")

def deque():
    global x
    global xf
    global yf
    global x0
    global x1
    global list1
    global listele
    global lenele
    global popped

    lenele=len(listele)-1
    length=len(list1)
    lenghtfront= len(listfront)
    canvas.delete(list1[0])
    canvas.delete(popped)

    xf+=60
    if xf<=x-60:
        canvas.delete(listfront[0])
        listfront.pop(0)

    # x-=60
    # x0-=60
    # x1-=60
    list1.pop(0)

    # if x > 40:

    if xf<=x-60:
        txtfront=canvas.create_text(xf+30,yf-90, text="FRONT", fill="red")
        listfront.append(txtfront)


    popped=canvas.create_text(700,300, text="The dequeued element was: "+str(listele[lenele]), fill="white")


    listele.pop()

    print(listele)
    # print(listrear)
    # print(x)
    # print("***")

def create ():
    return
    n=int(sizeEntry.get())
    x0=40
    y0=40
    x1=100
    y1=100
    for i in range(n):
        canvas.create_rectangle(x0,y0,x1,y1 ,fill="black",outline="white")
        x0+=60
        x1+=60

def clear():
    global x
    global xf
    global yf
    global x0
    global x1
    global y1
    global y0
    global listfront
    global list1
    global listele
    global pointer
    pointer=0
    listele=[]
    listfront=[]
    list1=[]
    x=40
    y=160
    xf=40
    yf=160
    list1=[]
    x0=40
    y0=100
    x1=100
    y1=160
    canvas.delete("all")


# canvas.create_rectangle(40,40,100,100 ,fill="black",outline="white")
# canvas.create_rectangle(100,40,100+60,100,fill="black",outline="white")
# canvas.create_rectangle(160,40,100+60+60,100,fill="black",outline="white")




# label= Label(ui_frame, text= "Size: ",bg="grey").grid(row=0,column=0,pady=5,sticky= W)
# sizeEntry= Entry(ui_frame)
# sizeEntry.grid(row=0,column=1,pady=5)

label= Label(ui_frame, text= "Element: ",bg="grey").grid(row=0,column=0,pady=5,padx=10,sticky= W)
eleEntry= Entry(ui_frame)
eleEntry.grid(row=0,column=1,padx=10,pady=5)

button_exit=Button(ui_frame, text = "  Enqueue  ",bg="#ff3232",fg="white", command=enque)
button_exit.grid(row=0,column=2,padx=10,pady=15,ipadx=10)

button_exit=Button(ui_frame, text = "  Dequeue  ",bg="#ff3232",fg="white", command=deque)
button_exit.grid(row=0,column=3,padx=10,pady=15,ipadx=10)

# button_exit=Button(ui_frame, text = "Create", command=create)
# button_exit.grid(row=1,column=3,padx=10,pady=10,ipadx=10)

button_exit=Button(ui_frame, text = "Exit",bg="#323232",fg="white", command=root.quit)
button_exit.grid(row=2,column=1,padx=50,ipady=2,pady=10,ipadx=40)

button_exit=Button(ui_frame, text = "Clear",bg="#323232",fg="white", command=clear)
button_exit.grid(row=2,column=2,padx=5,pady=10,ipady=2,ipadx=40)


root.mainloop()
