import time


def bubble(data, drawData, timetick):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):

            if data[j]>data[j+1]:
                 data[j],data[j+1] = data[j+1],data[j]
                 drawData(data,["#7CFC00" if x==j or x==j+1 else "#FF4500" for x in range(len(data))])  #green #red #FF4500
                 time.sleep(timetick)
    drawData(data, ["#7CFC00" for x in range(len(data))])  #green
#00ff45
#7CFC00
