set_1={1,2,3,4,5,5,6,7,'sa','sa'}
print(set_1)
print(len(set_1))
print(type(set_1))

set_1.remove('sa')
print(set_1)
set_1.add('sathish')
print(set_1)

set_1.pop()                                                # pop remove randomly
print(set_1)

set_2={'a','b','c','d'}
one=set_1.union(set_2)
print(one)

list=[1,2,3,4,5]

set_2.update(list)
print(set_2)


# we can not do append and del in set 