# create a list mylist
mylist = ["Dibyendu", "Day", 10, "March", 1995, "Quality Assurance Engineer", 93248]

# check the type of the variable mylist using the type class
print(type(mylist))

# raise an assertion if the type of the object mylist is not equal to List
assert type(mylist) is list, "Type Unmatched"  # do not compare types, use is/is not

print(f"{mylist}: TYPE MATCHED")

# Update the object in the 1st index of the list mylist from "Day" to "Dey"
mylist[1] = "Dey"
assert mylist[1] == "Dey", f"mylist update operation failed: {mylist}"
print(f"{mylist}: List has been successfully updated and modified")

# Append a value "Jharna" to the list

mylist.append("Jharna Dey")
print(mylist)

# del the object at the last index
del mylist[-1]
print(mylist)
