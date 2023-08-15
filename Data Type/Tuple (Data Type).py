tuple_1=('sathish',"umaiyal","aathini")

print(type(tuple_1))
print(len(tuple_1))

print(tuple_1)


l=list(tuple_1)
l[0]='SATHISHKUMAR'
tuple_1=tuple(l)
print(tuple_1)

''' unpacking tuuple '''

tuple_1=('sathish',"umaiyal","aathini")

(name1,name2,name3)=tuple_1
print(name1)
print(name2)
print(name3)
print('-------------------------------')
tuple_2=('sathish',"umaiyal","aathini","aathiran")
(name1,name2,*name3)=tuple_2
print(name1)
print(name2)
print(name3)

(name1,*name2,name3)=tuple_2
print(name1)
print(name2)
print(name3)