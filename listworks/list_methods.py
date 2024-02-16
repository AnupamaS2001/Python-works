colors=["red","greeen","blue","red"]

# methods
#===========

# append()--> to insert element in the last
# lst_obj.method_name()

colors.append("yellow")
print(colors)

# count()-->to count the objts in the list

print(colors.count("red"))

# index()--> to print the index value of the element(first occurence)

print(colors.index("blue"))

# insert(index,object)-->insert a index and obj at any position

colors.insert(3,"orange")
print(colors)

# sort()-->to sort the list

colors.sort()
print(colors)

# remove(object)-->to remove the first occurence of the object

colors.remove("red")
print(colors)

# pop(index)-->to remove the object in the base of index num (default value=-1)

colors.pop(2)
print(colors)

#copy()--> to copy the list

cpy_colors=colors.copy()
print(cpy_colors)

a=10
b=10
#a==b==> to cxheck the values are same
#a is b--> to check the adress value of the object
