#queue

T = int(input())
li = [i for i in range(1,T+1)]

h = 0;
t = T-1;
while(1):
    if(h >= t):
        print(li[h-1])
        break
    
    h+=1
    li.append(li[h])
    
    h+=1;
    t +=1;
        
    