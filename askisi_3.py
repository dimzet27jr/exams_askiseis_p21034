import string
import random

text_characters=string.ascii_letters + " "
with open ("two_cities_ascii.txt") as f:
    data=f.read()
new_txt=""

for c in data:
    if c in text_characters:
        new_txt=new_txt + c
words=new_txt.split(" ")

for i in range (0,len(words)):
    n=random.randrange(0,len(words))
    k=random.randrange(0,len(words))

    while n==k:
        n=random.randrange(0,len(words))
        k=random.randrange(0,len(words))
    gram=len(words[n])+ len(words[k])
    i=0
    
    if gram==20:
        words.remove(words[n])
        if k!= i in range (0,len(words)):
            words.remove(words[k-1])
        else:
            words.remove(words[k])
    
pl1=pl2=pl3=pl4=pl5=pl6=0

for i in range (0,len(words)):
    if len(words[i])==1:
        pl1=pl1 + 1
    elif len(words[i])==2:
        pl2=pl2 + 1
    elif len(words[i])==3:
        pl3=pl3 + 1
    elif len(words[i])==4:
        pl4=pl4 + 1
    elif len(words[i])==5:
        pl5=pl5 + 1
    else:
        pl6=pl6 + 1
print("In the new text there are",pl1,"words with one letter")
print("In the new text there are",pl2,"words with two letters")
print("In the new text there are",pl3,"words with three letters")
print("In the new text there are",pl4,"words with four letters")
print("In the new text there are",pl5,"words with five letters")
print("In the new text there are",pl6,"words with six or more letters")

    
