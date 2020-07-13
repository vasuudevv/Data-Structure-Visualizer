from tkinter import*
from tkinter import ttk
import random
from tkinter import messagebox
from bubble import bubble
from quick import quick
from merge import mergesort

root =Tk()
root.title("Sorting Visualizer")
root.maxsize(1000,800)            #opening window
root.config(bg="black")
#variables

selected_alg = StringVar()
data=[]

def drawData(data, colorArray):
    canvas.delete("all")
    c_height=380
    c_width=800
    x_width= c_width / (len(data)+1)
    offset= 30
    spacing=5
    normalizeData=[i/max(data) for i in data]
    for i, height in enumerate(normalizeData):

        x0=i * x_width + offset + spacing
        y0=c_height - height * 340
        x1=(i+1) * x_width + offset
        y1= c_height
        canvas.create_rectangle(x0,y0,x1,y1, fill=colorArray[i])
        canvas.create_text(x0+2,y0,anchor= SW, text=str(data[i]))

    root.update_idletasks()

def generate():
    global data
    minval= int(minEntry.get())
    maxval= int(maxEntry.get())
    size  = int(sizeEntry.get())

    if minval > maxval: maxval,minval = minval,maxval

    data=[]
    for _ in range(size):
        data.append(random.randrange(minval,maxval+1))
    drawData(data,["#ff3232" for x in range(len(data))])      #red


def startalgo():
    global data
    if not data: return
    timetick=speedScale.get()
    algo = algMenu.get()
    if algo == "":
        response=messagebox.showwarning("Warning","Please select the Algorithm")
    if algo == "Bubble Sort":
        bubble(data, drawData, timetick)
    if algo == "Merge Sort":
        mergesort(data,drawData,timetick)
    if algo == "Quick Sort":
        quick(data,0,len(data)-1,drawData,timetick)

    drawData(data,["#7CFC00"for x in range(len(data))])  #green

def color():
    return

#frame base layout
ui_frame= Frame(root, width=600, height=200,bg="grey")
ui_frame.grid(row=0,column=0,padx=10,pady=5,ipadx=5)

#canvas
canvas= Canvas(root, width=800, height= 380, bg="white")
canvas.grid(row=1, column=0,padx=10, pady=5)

bottom_frame= Frame(root, width=600, height=70,bg="grey")
bottom_frame.grid(row=2,column=0,padx=10,pady=5)

#UI Area
#row[0]
label= Label(ui_frame, text= "Algorithm:",bg="grey")
labelfont = ('arial', 10)
label.config(font = labelfont)
label.grid(row=0,column=0,pady=5,padx=5,sticky= W)

algMenu=ttk.Combobox(ui_frame, textvariable=selected_alg, values=["Bubble Sort", "Merge Sort","Quick Sort"])
algMenu.grid(row=0,column=1,padx=5,pady=5)
#algMenu.current(0)

speedScale= Scale(ui_frame, from_=0.1, to=2.0, length=200, digits= 2, resolution= 0.2,orient=HORIZONTAL, label="Select Speed [s]")
speedScale.grid(row=0,column=2, padx=5,pady=5)
Button(ui_frame, text="   Start   ",command=startalgo,bg="#ff3232",fg="white").grid(row=0, column=3,padx=5,pady=5)



#row[1]
#label= Label(ui_frame, text= "Size ",bg="grey").grid(row=1,column=0,padx=5,pady=5,sticky= W)
#sizeEntry= Entry(ui_frame)
sizeEntry= Scale(ui_frame, from_=3, to=25, resolution= 1,orient=HORIZONTAL, label="Size")
sizeEntry.grid(row=1,column=0,padx=5,pady=5)

# label= Label(ui_frame, text= "Min Value ",bg="grey").grid(row=1,column=2,padx=5,pady=5,sticky= W)
# minEntry= Entry(ui_frame)
minEntry= Scale(ui_frame, from_=0, to=100, resolution= 1,orient=HORIZONTAL, label="Min Value")
minEntry.grid(row=1,column=1,padx=5,pady=5)

# label= Label(ui_frame, text= "Max Value ",bg="grey").grid(row=1,column=4,padx=5,pady=5,sticky= W)
# maxEntry= Entry(ui_frame)
maxEntry= Scale(ui_frame, from_=3, to=100, resolution= 1,orient=HORIZONTAL, label="Max Value")
maxEntry.grid(row=1,column=2,padx=5,pady=5)

Button(ui_frame, text=" Generate ",command=generate,bg="#ff3232",fg="white").grid(row=1, column=3,padx=5,pady=5)

#bottom_frame
label1= Label(bottom_frame, text= "Bubble Sort:",bg="grey",fg="white")
label1.grid(row=0,column=0,pady=5,padx=5)

Button(bottom_frame, text = "    ",bg="#7CFC00", command=color).grid(row=1,column=0,padx=5)  #green
Label(bottom_frame, text=" Selected elements ").grid(row=1,column=1,padx=5)
Button(bottom_frame, text = "    ",bg="#FF4500", command=color).grid(row=1,column=2,padx=5)  #red
Label(bottom_frame, text=" Rest ").grid(row=1,column=3,padx=5)

label2= Label(bottom_frame, text= "Merge Sort:",bg="grey",fg="white")
label2.grid(row=2,column=0,padx=5)

Button(bottom_frame, text = "    ",bg="#FA8072", command=color).grid(row=3,column=2,padx=5) #pink
Label(bottom_frame, text=" Right Subarray ").grid(row=3,column=3,padx=5)
Button(bottom_frame, text = "    ",bg="yellow", command=color).grid(row=3,column=0,padx=5) #yellow
Label(bottom_frame, text=" Left Subarray ").grid(row=3,column=1,padx=5)
Button(bottom_frame, text = "    ",bg="#7CFC00", command=color).grid(row=3,column=4,padx=5)   #green
Label(bottom_frame, text=" Sorted Elements of Subarray ").grid(row=3,column=5,padx=5)

label3= Label(bottom_frame, text= "Quick Sort:",bg="grey",fg="white")
label3.grid(row=4,column=0,padx=5)

Button(bottom_frame, text = "    ",bg="#DCDCDC", command=color).grid(row=5,column=4,padx=5)   #grey
Label(bottom_frame, text=" Current Subarray ").grid(row=5,column=5,padx=5)

Button(bottom_frame, text = "    ",bg="#FF4500", command=color).grid(row=5,column=8,padx=5)   #red
Label(bottom_frame, text=" Border ").grid(row=5,column=9,padx=5)

Button(bottom_frame, text = "    ",bg="#6A5ACD", command=color).grid(row=5,column=2,padx=5) #blue
Label(bottom_frame, text=" Pivot ").grid(row=5,column=3,padx=5)

Button(bottom_frame, text = "    ",bg="#DAA520", command=color).grid(row=5,column=0,padx=5) #yellow
Label(bottom_frame, text=" Current Index ").grid(row=5,column=1,padx=5)

Button(bottom_frame, text = "    ",bg="#7CFC00", command=color).grid(row=5,column=6,padx=5)  #green
Label(bottom_frame, text=" Swapped Elements ").grid(row=5,column=7,padx=5)


button_exit=Button(bottom_frame, text = "  Exit  ",bg="#323232",fg="white", command=root.quit)
button_exit.grid(row=6,column=4,pady=5,ipadx=20,ipady=5)





root.mainloop()
