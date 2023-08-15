''' Transfer statement
1. break
2.continue
3.pass
'''

# pass statement
def sai ():
    print('sathshkumar')

def sam():
    pass

sai()


'''continue statement'''

for i in "sathishkumar":
    if i=="s" or i=="h":
        continue
    print(i)



name="sathishkumar"
A=0
while len(name)>A:
    if name[A]=="s" or name[A]=="h":
        A += 1
        continue

    print(name[A])
    A+=1

A=0
while A<5:
    if A==3:
        break
    A+=1
    print(A)