import random

pl_officer=pl_tower=0
print("In a 8*8 chessboard the results are:")
for i in range(100):        
    'For the position of the officer'

    officer_x=random.randrange(1,9)
    officer_y=random.randrange(1,9)

    'For the position of the tower'

    tower_x=random.randrange(1,9)
    tower_y=random.randrange(1,9)  

    'If officer can take down the tower'
    if (tower_x - officer_x == tower_y - officer_y):
        pl_officer= pl_officer + 1
    elif (-tower_x + officer_x == tower_y - officer_y):
        pl_officer= pl_officer + 1

    'If tower can take down the officer'
    if tower_x == officer_x:
        pl_tower= pl_tower + 1
    elif tower_y == officer_y:
        pl_tower= pl_tower + 1
    
print("The officer takes down the tower",pl_officer,"times")
print("The tower takes down the officer",pl_tower,"times")     

'''For a 7*7 chessboard'''

print(" ")
print("In a 7*7 chessboard the results are:")
pl_officer1=pl_tower1=0

for i in range (100):
    'For the position of the officer'

    officer1_x=random.randrange(1,8)
    officer1_y=random.randrange(1,8)

    'For the position of the tower'

    tower1_x=random.randrange(1,8)
    tower1_y=random.randrange(1,8)

    'If officer can take down the tower'
    if (tower1_x - officer1_x == tower1_y - officer1_y):
        pl_officer1= pl_officer1 + 1
    elif (-tower1_x + officer1_x == tower1_y - officer1_y):
        pl_officer1= pl_officer1 + 1

    'If tower can take down the officer'
    if tower1_x == officer1_x:
        pl_tower1= pl_tower1 + 1
    elif tower1_y == officer1_y:
        pl_tower1= pl_tower1 + 1
    
print("The officer takes down the tower",pl_officer1,"times")
print("The tower takes down the officer",pl_tower1,"times")

'''For a 7*8 chessboard'''

print(" ")
print("In a 7*8 chessboard the results are:")

pl_officer2=pl_tower2=0

for i in range (100):
    'For the position of the officer'

    officer2_x=random.randrange(1,8)
    officer2_y=random.randrange(1,9)

    'For the position of the tower'

    tower2_x=random.randrange(1,8)
    tower2_y=random.randrange(1,9)  

    'If officer can take down the tower'
    if (tower2_x - officer2_x == tower2_y - officer2_y):
        pl_officer2= pl_officer2 + 1
    elif (-tower2_x + officer2_x == tower2_y - officer2_y):
        pl_officer2= pl_officer2 + 1

    'If tower can take down the officer'
    if tower2_x == officer2_x:
        pl_tower2= pl_tower2 + 1
    elif tower2_y == officer2_y:
        pl_tower2= pl_tower2 + 1
    
print("The officer takes down the tower",pl_officer2,"times")
print("The tower takes down the officer",pl_tower2,"times")   
