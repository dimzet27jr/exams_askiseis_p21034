import string

chars_used=string.ascii_letters + "0123456789"
with open("two_cities_ascii.txt") as f:
    data=f.read()
new_txt=""

for c in data:
    if c in chars_used:
        new_txt=new_txt +c
words=new_txt


bin_text=''.join(format(ord(c), 'b') for c in words)

max0=0
max1=0
pl0=0
pl1=0

for i in range (0,len(bin_text)):
    if (bin_text[i]=="0"):
        pl0=pl0 + 1
        pl1=0
    else:
        pl1=pl1 + 1
        pl0=0

    if pl0>max0:
        max0=pl0

    elif pl1>max1:
        max1=pl1

print("The largest sequence with continuous 0s is:",max0)
print("The largest sequence with continuous 1s is:",max1)
    
