def working(list2,a,list3):
    for i in range(len(list2)):
        if(list2[i][0]==a):
            list3.append(list2[i])
        
    return list3


def working2(list2,a,list3):
    add=0
    swap=""
    list5=list(list4)
    for i in range(len(list2)):
        if(list2[i][0]==a):
            add=list5[-1]+list2[i][-1]
            list5[-1]=list2[i][-2]
            list5.append(add)
            
            
            list3.append(list5)
            add=0
            list5=list(list4)
        
    return list3

def findmin(list3,a):
    num=list3[0][-1]
    r_value=0
    for i in range(len(list3)):
        if(list3[i][-1]<num):
            r_value=i
            num=list3[i][-1]
    d=list3[r_value]
    
    list3.pop(r_value)
    return d


list2=[
    ('JFK', 'ATL', 150),
    ('ATL', 'SFO', 400),
    ('ORD', 'LAX', 200),
    ('LAX', 'DFW', 80),
    ('JFK', 'HKG', 800),
    ('ATL', 'ORD', 90),
    ('JFK', 'LAX', 500),
]


a="JFK"

k=3

list3=[]
list4=[]

b="LAX"


list3=working(list2,a,list3)
while(True):
    list4=findmin(list3,a)
    a=list4[-2]
    if(a==b):
        if(len(list4)<=k+2):        
            break
    list3=working2(list2,a,list3)



print(list4)



