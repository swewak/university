import random
def monty_hall(amount:int=10000):
    cnt1 = 0
    cnt2 = 0
    allcnt = 0
    for i in range(amount):
        prize=random.randrange(1,4)
        door1=random.randrange(1,4)
        if prize!=door1:
            door2=6-prize-door1
        else:
            door2=random.choice([prize+1,prize-1])
        xxx=random.randrange(1,3)
        if xxx==1:
            if door1==prize:
                cnt1+=1
                allcnt+=1
        else:
            if 6-door1-door2==prize:
                cnt2+=1
                allcnt+=1
    percent1=int((cnt1/allcnt)*100)
    percent2 = int((cnt2/allcnt)*100)
    return percent1,percent2