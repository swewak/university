import random
def birthday(x,pplcnt):
    allcnt=0
    for i in range(x):
        cnt = 0
        bday=[[random.randrange(1,29),random.randrange(1,13)] for y in range(pplcnt+1)]
        for k in range(1,pplcnt):
            for k1 in range(k+1,pplcnt+1):
               if bday[k]==bday[k1]:
                    cnt+=1
        if cnt>0:
            allcnt+=1
    prcnt=int((allcnt/x)*100)
    return prcnt