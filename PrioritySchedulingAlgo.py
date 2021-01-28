# STARVATION: there is chance that low priority never executes
# Solution: Aging: Time progress increases so Priority Increases

def PriorityScheduling(BurstTime):

    SortedBurstTime = sorted(BurstTime)
    waitingTime = [0]
    turnAroundTime = [0]

    for i in SortedBurstTime:
        waitingTime.append(waitingTime[-1] + i[1])
        turnAroundTime.append(turnAroundTime[-1] + i[1])

    waitTime= waitingTime.copy()


    waitingTime.pop()
    turnAroundTime.pop(0)

    avgWaitingTime = sum(waitingTime) / len(waitingTime)
    avgArrivalTime = sum(turnAroundTime)/len(turnAroundTime)
    return {'SortedProcess':SortedBurstTime,'waitingTime':waitTime,'avgWaitingTime':avgWaitingTime,'avgArrivalTime':avgArrivalTime,}
#BurstTime = [[4, 24], [1, 68], [3, 17], [2, 53]]
#[print(key,value) for key,value in PriorityScheduling(BurstTime).items()]