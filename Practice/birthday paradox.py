import random

def birthday(x):
    allcnt=0
    for i in range(x):
        cnt = 0
        bday=[[random.randrange(1,29),random.randrange(1,13)] for y in range(24)]
        for k in range(1,23):
            for k1 in range(k+1,24):
               if bday[k]==bday[k1]:
                    cnt+=1
        if cnt>0:
            allcnt+=1
    prcnt=(allcnt/x)*100
    return prcnt
print(birthday(1000))
