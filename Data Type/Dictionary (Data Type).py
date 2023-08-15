dict={1:"sathish",2:"umaiyal",3:'aathini',4:'aathiran'}

print(type(dict))
print(len(dict))

print(dict.keys())
print(dict.values())
print(dict[1])
print(dict[4])

ok=dict.items()
print(ok)


dict.update({5:"amma"})
print(dict)

dict.pop(3)
print(dict)

dict.popitem()                                # pop item removes the last insertitem
print(dict)

del dict[1]
print(dict)

dict.clear()
print(dict)

nd={"family_1":{1:'sridevi',2:'chidamabaram'},"family_2":{1:"sasi",2:"silambarasi"},"familt_3":{1:'umaiyal',2:"sathish"}}
print(nd)
print(len(nd))

print(nd.keys())
print(nd.values())

