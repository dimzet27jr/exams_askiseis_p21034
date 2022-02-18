import random

w1=0
w2=0
draw=0
for i in range(100):
    xartia=[]
    figures=["J", "Q", "K"]
    xarti=[i for i in range(1,11)]+ figures
    color=["H", "S", "C", "D"]
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    random.shuffle(xartia)
    player1=[]
    sum1=0
    while sum1<16:
        sum1=0
        player1.append(xartia.pop())
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
    if sum1>21:
        w2=w2+1
    else:
        player2=[]
        sum2=0
        while sum2<16:
            sum2=0
            player2.append(xartia.pop())
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
        if sum2>21:
            sum2=0
        if sum1>sum2:
            w1=w1+1
        elif sum2>sum1:
            w2=w2+1
        else:
            draw=draw+1
            
print("Player 1 has won", w1, "games")
print("Player 2 has won", w2, "games")
print("The game end in draw", draw, "times")
print(" ")

print("In a modified version of the game where player1 starts with a figure or 10 and player 2 starts with a number the results are:")      
print(" ")
w1=0
w2=0
draw=0
for i in range (100):
    xartia=[]
    a=[]
    b=[]
    figures=["J", "Q", "K"]
    tens=["10", "J", "Q", "K"]
    numbers=[i for i in range(1,10)]
    xarti=[i for i in range(1,11)]+ figures
    color=["H", "S", "C", "D"]
    for i in tens:
        for j in color:
            a.append([i,j])
    random.shuffle(a)
    for i in numbers:
        for j in color:
            b.append([i,j])
    random.shuffle(b)
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    random.shuffle(xartia)
    
    player1=[]
    player1.append(a.pop())
    temp=player1[0]
    x=0
    while x<len((xartia)):
        if xartia[x]==temp:
            xartia.pop(x)
        else:
            x=x+1
    
    sum1=0
    while sum1<16:
        sum1=0
        player1.append(xartia.pop())
        for card in player1:
            if card[0] in tens:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
    if sum1>21:
        w2=w2+1
    else:
        player2=[]
        player2.append(b.pop())
        temp1=player2[0]
        k=0
        while k<len((xartia)):
            if xartia[k]==temp1:
                xartia.pop(k)
            else:
                k=k+1
        sum2=0
        while sum2<16:
            sum2=0
            player2.append(xartia.pop())
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
        if sum2>21:
            sum2=0
        if sum1>sum2:
            w1=w1+1
        elif sum2>sum1:
            w2=w2+1
        else:
            draw=draw+1
    
print("Player 1 has won", w1, "games")
print("Player 2 has won", w2, "games")
print("The game end in draw", draw, "times")














