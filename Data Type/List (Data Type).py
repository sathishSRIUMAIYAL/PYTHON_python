list_1=["A","B","c","d"]

print(list_1)
print(type(list_1))
print(len(list_1))

''' Access list items '''
list_1=["A","B","c","d"]
print(list_1[1])
print(list_1[-1])
print(list_1[1:3])

list_1[1]="BBB"
print(list_1)

list_1[1:3]=["BBB","CCC"]
print(list_1)

list_1[1:2]=['B','C']
print(list_1)

list_1[1:3]='Z'
print(list_1)

The_list=['apple','orange','pineapple','papaya']
The_list.append('perry')
print(The_list)
The_list.insert(1,"pine")
print(The_list)

The_list.remove("pine")
print(The_list)
The_list.pop(4)
print(The_list)

del The_list[0]
print(The_list)

The_list.sort()
The_list.sort(reverse=True)
print(The_list)

The_list.clear()
print(The_list)