b=int(input())
s=i=j=0
while b!=0:
     i=b%10
     s=s+i*(2**j)
     b=b//10
     j+=1
print(s)

