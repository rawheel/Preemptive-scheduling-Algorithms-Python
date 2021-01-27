def ShortestJobFirst(BurstTime):
    sortedBtList ={}
    for key in sorted(BurstTime):
        sortedBtList[key] =BurstTime[key]
    return(sortedBtList)
BurstTime = {3:6,2:8,1:7,4:3}
ShortestJobFirst((BurstTime))
