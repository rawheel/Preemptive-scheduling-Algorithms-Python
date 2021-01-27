def round_robin(process, quantumTime):
    final_lst = []
    t_lst = []
    timeQueue = [0]

    def run(process):
        temp_dict = {}
        #print(process, 'process')
        for prcs, burstTime in process.items():
            newBurstTime = burstTime - quantumTime

            if newBurstTime <= 0:
                final_lst.append(prcs)
            else:
                temp_dict[prcs] = newBurstTime
            t_lst.append(prcs)
            # To Handle Time queue
            remain = timeQueue[-1]

            if newBurstTime < 0:
                remain = remain + quantumTime + newBurstTime
                timeQueue.append(remain)
            else:
                remain += quantumTime
                timeQueue.append(remain)

        process = temp_dict
        #print(final_lst)

        return process

    a = run(process)
    while True:
        if len(a) != 0:
            a = run(a)
        else:
            break
    '''print()
    print(f'Empty Sequence: {final_lst}')
    print(f'Final Sequence:{t_lst}')
    print(f'Time Sequence: {timeQueue}')'''
    return {'EmtpySequence':final_lst,'Final Sequence':t_lst,'TimeSequence':timeQueue}


process = {'p1':53,'p2':17,'p3':68,'p4':24}
#process = {'p1': 24, 'p2': 3, 'p3': 3}
q_time = 20

round_robin(process, q_time)
