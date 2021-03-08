import math,random


arrival_rate=0.2        #0.2pkt/slot time
service_rate=0.5        #0.5pkt/slot time


def gen_arrival_interval():
    p=random.random()
    return -(1/arrival_rate)*math.log(1-p,math.e)

def gen_service_time():
    p=random.random()
    return -(1/service_rate)*math.log(1-p,math.e)

total=100  #slot time


current_event=None    #1 arrival  2 departure
next_event=None       #1 arrival  2 departure
system_state=False   #idle
i=0

pkt_queue=[]
arrivial_queue=[]
departure_queue=[]

while(i<total):
    current_event=next_event
    if current_event==1: #處理arrivial
    
        if system_state:             #busy
            t2=departure_queue[0]
            if arrivial_queue and arrivial_queue[-1]<t2:
                t1=gen_arrival_interval()+arrivial_queue[-1]
                arrivial_queue.append(t1)
            if arrivial_queue and arrivial_queue[-1]>=t2:
                t1=arrivial_queue[-1]
            if not arrivial_queue:
                t1=gen_arrival_interval()+i
                arrivial_queue.append(t1)
            
                
            if t1<t2:
                next_event=1
                i=t1
            else:
                next_event=2
                i=t2
                departure_queue.pop(0)
        
        
        else:                       #空
            t1=i+gen_arrival_interval()
            t2=i+gen_service_time()
            arrivial_queue.append(t1)
            system_state=True
            if t1<t2:
                next_event=1
                i=t1
                departure_queue.append(t2)
            else:
                next_event=2
                i=t2
                
            
                    
    elif current_event==2:
        if arrivial_queue:     #arrivial_queue一定有東西
            t1=arrivial_queue.pop(0)
            if t1<=i:
                next_event=1
                departure_queue.append(gen_service_time()+i)
                #i不變
            else:
                system_state=False
                next_event=1
                i=t1
                    
    else:
        t11=i+gen_arrival_interval()
        t1=t11+gen_arrival_interval()
        t2=t11+gen_service_time()
        arrivial_queue.append(t1)
        system_state=True
        if t1<t2:
            next_event=1
            i=t1
            departure_queue.append(t2)
        else:
            next_event=2
            i=t2
        
        
        
        
        
        
        
        