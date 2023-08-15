
''' Arithematic operators '''

print(10+10)            # addition
print(10-10)            # subtraction
print(10/10)            # division
print(10//10)           # floor division
print(10*10)            # multiplication
print(10%10)            # module
print(10**10)           # exponent

''' comparision operators '''

print(10>5)
print(10<15)
print(10<=10)                       # < or =
print(10>=50)
print(100==10)
print(100!=100)

''' Assignment operators  '''

a=10
a+=1
a-=1
a/=1
a//=1
a*=1
a**=1
a%=1


"""logic operators """

print(10>5 and 10<50)                           # and
print(10<5 or 10>5)                             # or
print(not 10>10 and 20<50)                      # not

""" bitwise operators """

print(bin(2))
print(bin(3))

print(2&3)                                    # and
print(2|3)                                    # or
print(2^3)                                    # xor
print(~20)                                    # not
print(20<<2)                                  # left shift
print(20<<3)
print(20>>2)                                  # right shift
print(20>>3)


''' identity operators '''

A=[1,2,3,4]
B=A
c=[5,6,7,8]
print(A is B )
print(A is c)
print(id(A))
print(id(B))
print(id(c))

# it same every item

a=(1,2,3)
b=a
x=(6,6,7,8)
z=(1,2,3)

print(a is b)
print( a is x)
print(a is z)

print(id(a))
print(id(z))


""" membership operators """


name=['sathish','kumar','ran']

print('ram' in name)
print('Ran' in name)
print('ran' in name)
print('  ran' in name)

print('sathish' not in name)
print('ram' not in name)

if 'sathish' in name:
    print(' yes sathis is a one of the member ')
else:
    print('sorry')

