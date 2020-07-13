import pydot
from tkinter import *
from tkinter import Entry
from tkinter import ttk
from PIL import ImageTk,Image
import random
from tkinter import messagebox

plot= Tk()
plot.title("graph")
plot.config(bg="black")
plot.maxsize(1500,1500)

#graph variable and functions

selected_alg = StringVar()


def addnodes():   #add nodes in the graph
    global graph
    global nodes
    global list1
    structure = structMenu.get()
    ststruct=""
    if structure == "":
        response1=messagebox.showwarning("Warning","Please select the Graph Structure")

    if structure == "Directed Graph" or structure == "Tree":  #initialize the graph structure
        ststruct ="digraph"

    elif structure == "Undirected Graph":
        ststruct ="graph"

    graph = pydot.Dot(graph_type=ststruct)

    list1=[]
    stnode=nodeEntry.get()
    nodes= int(nodeEntry.get())
    # if stnode == "":
    #     response2=messagebox.showwarning("Warning","Please enter number of nodes")
    if nodes <= 13:   #node limit
        for i in range(nodes):      #add the nodes
            name = "node"+str(i)
            globals()[name] = pydot.Node(str(i), style="filled", fillcolor="yellow",shape="circle")
            list1.append(globals()[name])
            graph.add_node(globals()[name])

    else:
        response3=messagebox.showwarning("Warning","  Node limit: 13  ")        #showinfo---showerror---showwarning---askquestion---askokcancel




def addEdge(graph,list1):

    global a
    global list_img
    global img1
    list_img = []
    # stx=xEntry.get()
    # sty=yEntry.get()
    x= int(xEntry.get())
    y= int(yEntry.get())

    # if stx =="" or sty=="":
    #     response4=messagebox.showwarning("Warning","Please enter the nodes")
    graph.add_edge(pydot.Edge(list1[x], list1[y]))

    a=random.random()
    graph.write_png('bin/'+str(a)+'.png')

    img1= ImageTk.PhotoImage(Image.open('bin/'+str(a)+".png"))
    list_img.append(img1)

def show(): #print graph
    label= Label(outframe,image= img1)
    label.grid(row=0, column=0,padx=20,pady=10)


#upper frame
ui_frame= Frame(plot, width=800, height=400,bg="grey")
ui_frame.grid(row=0,column=0,padx=5,pady=5,ipadx=5,ipady=5)

#middle output frame
outframe= Frame(plot, width=800, height= 400, bg="white")
outframe.grid(row=1, column=0,padx=10, pady=5,ipadx=5,ipady=5)

#bottom frame
bottom_frame= Frame(plot, width=800, height=400,bg="grey")
bottom_frame.grid(row=2,column=0,padx=5,pady=5,ipadx=5,ipady=5)

#input entries
label= Label(ui_frame, text= "  Nodes:  ",bg="white" ,fg="black",bd=3,relief=SUNKEN).grid(row=0,column=0,padx=5,pady=5,sticky= W)
nodeEntry= Entry(ui_frame)
nodeEntry.grid(row=0,column=1,padx=5,pady=5)

#add node button
Button(ui_frame, text="      Add Nodes      ",command=addnodes,bg="#ff3232",fg="white").grid(row=0, column=2,padx=5,pady=10,columnspan=2)

#x and y entries
label= Label(ui_frame, text= "  x:  ",bg="white" ,fg="black",bd=3,relief=SUNKEN).grid(row=1,column=0,padx=5,pady=5)#,sticky= W)
xEntry= Entry(ui_frame)
xEntry.grid(row=1,column=1,padx=5,pady=10)

label= Label(ui_frame, text= "  y:  ",bg="white" ,fg="black",bd=3,relief=SUNKEN).grid(row=1,column=2,padx=5,pady=5)#,sticky= W)
yEntry= Entry(ui_frame)
yEntry.grid(row=1,column=3,padx=5,pady=5)

#add edge button
Button(ui_frame, text="       Add Edge       ",command=lambda: addEdge(graph,list1),bg="#ff3232",fg="white").grid(row=1, column=4,padx=5,pady=5)
#show button
Button(ui_frame, text="       Show       ",command=show,bg="#323232",fg="white").grid(row=2, column=1,pady=5,ipadx=5,columnspan=3)
#structure label
structure= Label(bottom_frame, text="   Structure: " ,bd=3,relief=SUNKEN, anchor=W)
structure.grid(row=0, column=0,padx=20, sticky=W)
#dropdown menu
structMenu=ttk.Combobox(bottom_frame, textvariable=selected_alg, values=["Directed Graph", "Undirected Graph","Tree"])
structMenu.grid(row=0,column=1,padx=5,pady=5,sticky=W)
#exit
button_exit=Button(bottom_frame, text = "  Exit  ", bg="#323232",fg="white",command=plot.quit)
button_exit.grid(row=1,column=0,padx=50,ipady=2,pady=10,ipadx=40,columnspan=2)



plot.mainloop()
