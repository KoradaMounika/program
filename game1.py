import random
u=input()
l=['rock','paper','scissor']
a=random.randint(0,2)
c=l[a]
print(c)
if u not in l:
    print('enter correct option:')
else:
    if c=='rock' and u=='scissor':
        print('computer won')
    elif c=='paper' and u=='rock':
        print('computer won')
    elif c=='scissor' and u=='paper':
        print('computer won')
    elif c==u:
        print('Tie')
    else:
        print('user won')
