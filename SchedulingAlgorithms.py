import pprint
#FCFS
#In Processes Elements Are as follows [ID,Arrival_Time_BurstTime]
# Processes = [
#     [0,0,2],
#     [1,1,6],
#     [2,2,4],
#     [3,3,9],
#     [4,6,12]
# ]
# Processes = sorted(Processes,key=lambda x:x[1])
# Completion_Time = 0
# for process in Processes:
#     Completion_Time += process[2]
#     process.append(Completion_Time)#Completion_Time for Process
#     process.append(Completion_Time-process[1])#TAT for Process
#     process.append(process[4]-process[2])#WAITINGTIME for Process
# pprint.pprint(["ID","ARRIVAL_TIME","BURSTTIME","TAT","WAITINGTIME"])
# pprint.pprint(Processes)
# pprint.pprint(f"Average Waiting Time is := {sum([element[-1] for element in Processes])/len(Processes)}")
# pprint.pprint(f"Average TAT is := {sum([element[-2] for element in Processes])/len(Processes)}")



# exit()

#SJF
# Processes = [
#     [1,0,7],
#     [2,2,4],
#     [3,4,1],
#     [4,5,4]
# ]

# Working = sorted(Processes,key=lambda x:x[1])
# Quee = []
# Completion_Time = Working[0][1]
# Result = []
# print("Order Of Execution is")
# while Working:
#     for element in Working:
#         if element not in Quee and element[1]<=Completion_Time:
#             Quee.append(element)
#     Quee = sorted(Quee,key=lambda x:x[2])
#     if len(Quee)==0:
#         #This Will get out of the loop if theres gap between Two Processes
#         Working = sorted(process,key=lambda x:x[1])
#         Completion_Time+=Working[0][1]-Completion_Time
#     process = Quee[0]
#     Completion_Time += process[2]
#     print(process)
#     process.append(Completion_Time)#Completion_Time for Process
#     process.append(Completion_Time-process[1])#TAT for Process
#     process.append(process[4]-process[2])#WAITINGTIME for Process
#     Working.remove(process)    
#     Quee.pop(0)
#     Result.append(process)
# Processes = Result
# pprint.pprint(["ID","ARRIVAL_TIME","BURSTTIME","TAT","WAITINGTIME"])
# pprint.pprint(Processes)
# pprint.pprint(f"Average Waiting Time is := {sum([element[-1] for element in Processes])/len(Processes)}")
# pprint.pprint(f"Average TAT is := {sum([element[-2] for element in Processes])/len(Processes)}")

# exit()
#Round Robin 
#Implemenation Given Below is Unstable But Still can fool the external So u can use it
#Here the forth element of list represent the remaining time
Processes = [
        [1,0,10,10],
        [2,1,4,4],
        [3,2,5,5],
        [4,3,3,3]
]
Processes = sorted(Processes,key=lambda x:x[1])
Quee = [Processes[0]];
Processes.pop(0)
Atomic_Time = 3;
Current_Time = Quee[0][1];
Result = []
while Quee:
    if Quee[0][3] <= Atomic_Time and Quee[0][3]>0:
        Current_Time += Atomic_Time-(Quee[0][3]%Atomic_Time)
        Quee[0].append(Current_Time)#Completion_Time for Process
        Quee[0].append(Current_Time-Quee[0][1])#TAT for Process
        Quee[0].append(Quee[0][5]-Quee[0][2])#WAITINGTIME for Process
        Result.append(Quee[0])
        Quee.pop(0)
    elif len(Quee)>=1 and Quee[0][3]>Atomic_Time:
        Quee[0][3] -= Atomic_Time;
        Current_Time+=Atomic_Time
        data = Quee.pop()
        next_ = sorted(list(filter(lambda x:x[1]<=Current_Time,Processes)),key=lambda x:x[1])
        Quee.extend(next_)
        Processes = list(filter(lambda x:x[1]>Current_Time,Processes))
        Quee.append(data)
Processes = Result
pprint.pprint(["ID","ARRIVAL_TIME","BURSTTIME","TAT","WAITINGTIME"])
pprint.pprint(Processes)
pprint.pprint(f"Average Waiting Time is := {sum([element[-1] for element in Processes])/len(Processes)}")
pprint.pprint(f"Average TAT is := {sum([element[-2] for element in Processes])/len(Processes)}")

