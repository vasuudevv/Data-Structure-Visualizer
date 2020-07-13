import time
def mergesort(data,drawData,timetick):
     merge_process(data,0,len(data)-1,drawData,timetick)



def merge_process(data,left,right,drawData,timetick):

    if left < right:
        middle= (left+right) // 2
        merge_process(data,left,middle,drawData,timetick)
        merge_process(data,middle+1,right,drawData,timetick)
        merge(data,left,middle,right,drawData,timetick)

def merge(data,left,middle,right,drawData,timetick):

    drawData(data, getcolorArray(len(data),left,middle,right))
    time.sleep(timetick)

    leftpart=data[left:middle+1]
    rightpart=data[middle+1:right+1]

    leftidx=0
    rightidx=0

    for dataidx in range(left, right+1):
        if leftidx<len(leftpart) and rightidx < len(rightpart):
            if leftpart[leftidx] <= rightpart[rightidx]:

                data[dataidx] = leftpart[leftidx]
                leftidx+=1
            else:
                data[dataidx] = rightpart[rightidx]
                rightidx+=1

        elif leftidx < len(leftpart):
            data[dataidx]= leftpart[leftidx]
            leftidx+=1

        else:
            data[dataidx] = rightpart[rightidx]
            rightidx+=1
    drawData(data, ["#7CFC00" if x >= left and x <= right else "white" for x in range(len(data))])
    time.sleep(timetick)


def getcolorArray(length, left , middle, right):
    colorArray=[]

    for i in range(length):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colorArray.append("yellow")

            else:
                colorArray.append("#FA8072")    #pink

        else:
            colorArray.append("white")

    return colorArray
