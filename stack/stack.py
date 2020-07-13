from tkinter import*
from tkinter import ttk
import random
from tkinter import messagebox


root =Tk()
root.title("STACK")
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
list1=[]
x0=40
y0=100
x1=100
y1=160
listtop=[]
listele=[]
pointer=0
pointx=40

#functions
popped=canvas.create_text(700,300, text="The popped element was: ", fill="white")

def push():
    global x         #declare globals
    global nn
    global list1
    global x0
    global x1
    global y1
    global y0
    global listtop
    global txttop
    global listele
    global pointer
    global pointx

    listele.append(int(eleEntry.get()))  #get the element
    element=eleEntry.get()
    length=len(listtop)

    if len(listele)<=14:      # array limit
        canvas.create_rectangle(x0,y0,x1,y1 ,fill="black",outline="white")   #create the array box
        if len(listele)==pointer+1 :
            canvas.create_text(pointx+30,y+20, text=pointer,font=("arial", 12), fill="lightgreen")
            pointx+=60
            pointer+=1
        x0+=60
        x1+=60

        txt=canvas.create_text(x+30,y-30, text=element,font=("arial", 12), fill="orange")      #push the element
        txttop=canvas.create_text(x+30,y-75, text="TOP", fill="red")        #display top tag for the element on  the top

        listtop.append(txttop)    #delete occurence of top from previous position of top
        if length>1:
            canvas.delete(listtop[length-1])
        if length==1:
            canvas.delete(listtop[0])
        list1.append(txt)
        x+=60
    else:
        response=messagebox.showwarning("Warning","Array limit: 13")


def pop():
    global x
    global x0
    global x1
    global list1
    global listele
    global lenele
    global popped

    lenele=len(listele)-1
    length=len(list1)
    lenghttop= len(listtop)
    canvas.delete(list1[length-1])
    canvas.delete(listtop[lenghttop-1])
    canvas.delete(popped)

    x-=60
    x0-=60
    x1-=60

    list1.pop()
    listtop.pop()

    if x > 40:
        txttop=canvas.create_text(x-30,y-75, text="TOP", fill="red")
        listtop.append(txttop)


    popped=canvas.create_text(700,300, text="The popped element was: "+str(listele[lenele]), fill="white")



    listele.pop()

    # print(list1)
    print(listele)
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

    global x0
    global x1
    global y1
    global y0
    global pointer
    global listele
    global list1
    global pointx
    listele=[]
    list1=[]
    pointer=0
    pointx=40
    x=40
    y=160
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

label= Label(ui_frame, text= "Element: ",bg="grey").grid(row=0,column=0,pady=15,padx=10,sticky= W)
eleEntry= Entry(ui_frame)
eleEntry.grid(row=0,column=1,padx=10,pady=15)

button_exit=Button(ui_frame, text = "  Push  ",bg="#ff3232",fg="white", command=push)
button_exit.grid(row=0,column=2,padx=10,pady=15,ipadx=10)

button_exit=Button(ui_frame, text = "  Pop  ",bg="#ff3232",fg="white", command=pop)
button_exit.grid(row=0,column=3,padx=10,pady=15,ipadx=10)

# button_exit=Button(ui_frame, text = "Create", command=create)
# button_exit.grid(row=1,column=3,padx=10,pady=10,ipadx=10)

button_exit=Button(ui_frame, text = "Exit",bg="#323232",fg="white", command=root.quit)
button_exit.grid(row=2,column=1,padx=50,ipady=2,pady=10,ipadx=40)

button_exit=Button(ui_frame, text = "Clear",bg="#323232",fg="white",highlightcolor="yellow", command=clear)
button_exit.grid(row=2,column=2,padx=5,pady=10,ipady=2,ipadx=40)


root.mainloop()
