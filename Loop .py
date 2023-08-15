''' while loop '''


A=0
while A<5:
    print("sathish")
    A+=1

A=5
while A>0:
    print(A)
    A-=1

A=0
name='sathishkumar'
while len(name)>A:
    print(name[A])
    A+=1



tet="hello"

while tet in " hello":
    print('yes this is ')
    break



lat=' '
while not lat.isalpha():
    lat=input('enter your name:')
    print(lat)



import random
num=random.randint(1,20)
guess=int(input('enter your name'))
while guess!=num:
    if guess>num:
        print('this number is height try again')
    elif guess<num:
        print('this number is low try again')
    guess = int(input('enter your name'))
else:
    print('you won')





''' for loop '''

for i in range(10):
    print(i)

for i in range (5):
    print('sathish')

for i in "sathish":
    print(i)

name='sathishkumar'
A=0

for i in range(len(name)):
    print(name[0:A])
    A+=1

for i in range(len(name)):
    print(name[0:A])
    A-=1


for i in range(5):
    for j in range(i+1):
        print("$",end=" ")
    print(" ")

for i in range(5):
    for j in range(i,4):
        print("$",end=' ')
    print(' ')


for i in range(5):
    for j in range(i+1):
        print("#",end=' ')

    for j in range(i,4):
        print(" ",end=' ')

    for j in range(i,4):
        print(" ",end=' ')

    for j in range(i+1):
        print('#',end=' ')

    print(' ')

for i in range(5):
    for j in range(i,5):
        print("#",end=' ')

    for j in range(i):
        print(' ',end=' ')

    for j in range(i):
        print(" ",end=" ")

    for j in range(i,5):
        print("#",end=' ')

    print(' ')

for i in range(6):
    for j in range(i):
        print(j,end=' ')
    print(" ")

for i in range(6):
    for j in range(i):
        print(i,end=' ')
    print(" ")


for i in range(6):
    for j in range(1,i+1):
        print(j,end=' ')
    print(" ")


for i in range(6,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print(" ")

B=0
for i in range(6,0,-1):
    B += 1
    for j in range(1,i+1):
        print(B,end=' ')
    print("\r")

B=5
for i in range(6,0,-1):
    for j in range(0,i):
        print(B,end=' ')
    print("\r")