import random
l=[]
count=0
while len(l)<=90:
    a=random.randint(1,90)
    if a not in l:
        print(a,end=' ')
        l.append(a)
        count=count+1
print(count)
