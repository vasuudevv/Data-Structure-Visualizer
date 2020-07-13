import time

def partition(data, head, tail, drawData, timetick):
    border = head
    pivot=data[tail]

    drawData(data, getcolorArray(len(data),head, tail, border,border))
    time.sleep(timetick)

    for j in range(head,tail):
        if data[j] < pivot:
            drawData(data, getcolorArray(len(data),head, tail, border,j,True))
            time.sleep(timetick)

            data[border], data[j] = data[j], data[border]
            border+=1

            drawData(data, getcolorArray(len(data),head, tail, border,j))
            time.sleep(timetick)



    #swap pivot and border
    data[border], data[tail] = data[tail], data[border]

    drawData(data, getcolorArray(len(data),head, tail, border,tail,True))
    time.sleep(timetick)

    return border

def quick(data, head, tail, drawData, timetick):
    if head < tail:
        partitionIdx = partition(data, head, tail, drawData, timetick)
        #left partition
        quick(data, head, partitionIdx-1 , drawData, timetick)
        #right partition
        quick(data, partitionIdx+1 , tail, drawData, timetick)

def getcolorArray(datalen, head, tail, border, curridx, isSwap= False):

    colorArray=[]
    for i in range(datalen):
        #base color
        if i >= head and i <=tail:
            colorArray.append("#DCDCDC")  #grey
        else:
            colorArray.append("white")

        if i == tail:
            colorArray[i] = "#6A5ACD" #"#1E90FF"  #blue

        elif i == border:
            colorArray[i]="#FF4500"   #red

        elif i == curridx:
            colorArray[i]="#DAA520"  #yellow

        if isSwap:
            if i == border or i == curridx:
                colorArray[i] = "#7CFC00"  #green

    return colorArray
