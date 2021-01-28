from PrioritySchedulingAlgo import PriorityScheduling

from RoundRobin import round_robin
from sjf import ShortestJobFirst

class PreemptiveAlgorithms:
    def PriorityScheduling(self,BurstTime):
        print("*" * 50)
        print(" "*10,"Priority Scheduling Algorithm")
        print("*"*50)
        [print(key, value) for key, value in PriorityScheduling(BurstTime).items()]
        print("*" * 50)
        return PriorityScheduling(BurstTime)
    def RoundRobin(self,processes,quantumTime):
        print("*" * 50)
        print(" " * 10, "Round Robin Algorithm")
        print("*" * 50)
        [print(key, value) for key, value in round_robin(processes,quantumTime).items()]
        print("*" * 50)
        return round_robin(processes,quantumTime)
    def SJF(self,BurstTime):
        print("*" * 50)
        print(" " * 10, "Shortest Job First Algorithm")
        print("*" * 50)
        [print(key, value) for key, value in ShortestJobFirst(BurstTime).items()]
        print("*" * 50)
        return ShortestJobFirst(BurstTime)

#Preemptive Algorithm Object
PreemptiveObject = PreemptiveAlgorithms()

#calling PriorityScheduling from Preemptive Algorithm Object
BurstTime = [[4, 24], [1, 68], [3, 17], [2, 53]]
PreemptiveObject.PriorityScheduling(BurstTime)

#calling Round Robin from Preemptive Algorithm Object
processes = {'p1':53,'p2':17,'p3':68,'p4':24}
quantumTime = 20
PreemptiveObject.RoundRobin(processes,quantumTime)
#Accessing TimeSequence Attribute from Round Robin Algorithm
print(PreemptiveObject.RoundRobin(processes,quantumTime)['TimeSequence'])

#calling Shortest Job First from Preemptive Algorithm Object
BurstTime = {3:6,2:8,1:7,4:3}
PreemptiveObject.SJF(BurstTime)