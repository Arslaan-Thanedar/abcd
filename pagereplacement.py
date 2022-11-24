#FIFO page Replacement ;
string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1];
frame_ = [];
size = 3;
hits , faults = 0 , 0 ;
for idx in range(string.__len__()):
    if string[idx] in frame_:
        hits += 1 ; 
    else:
        faults += 1;
        if len(frame_)==size:
            frame_.pop(0);
        frame_.append(string[idx]);
print(f"Hits->{hits} faults->{faults}")
print(f"Hit Rate -> {hits/(hits+faults)*100}%")

#LRU Page Replacement
string =  [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
frame_ = [];
size = 4;
hits , faults = 0 , 0 ;
for idx in range(len(string)):
    if string[idx] in frame_:
        hits+=1;
    else:
        faults += 1 ;
        if len(frame_)==size:
            storage = []
            for i in string[:idx][::-1]:
                if len(storage)==size-1:
                    break
                else:
                    if i not in storage:
                        storage.append(i)
            frame_.remove([i for i in frame_ if i not in storage][0])
        frame_.append(string[idx]);
print(f"Hits->{hits} faults->{faults}")
print(f"Hit Rate -> {hits/(hits+faults)*100}%")

#Optimal Page Replacement
string =  [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
frame_ = [];
count_ = [];
size = 4;
hits , faults = 0 , 0 ;
for idx in range(len(string)):
    if string[idx] in frame_:
        hits+=1;
    else:
        faults+=1;
        if len(frame_)==size:
            track = set()
            order_ = []
            future = [i for i in string[idx+1:] if i in frame_]
            for i in future:
                if i not in track:
                    track.add(i)
                    order_.append(i)
            future = order_
            if len(future)==size:
                frame_.remove(future[-1])
            else:
                data = list(set(frame_).difference(set(future)))
                frame_.remove(data[0])
        frame_.append(string[idx])
print(f"Hits->{hits} faults->{faults}")
print(f"Hit Rate -> {hits/(hits+faults)*100}%")
