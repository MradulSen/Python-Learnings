d1 = {}  # dict init empty

d2 = dict() #create empty dict

my_dict = {
    "name" : "Mradul",
    "role" : "Support",
    "city" : "Pune"
}

print(my_dict["name"]) #method 1

print(my_dict.get("role")) #method 2  time complexity is good (Big(O)=1)

my_dict["salary"] = 2000
my_dict["name"] = "Mradul Sen"
print(my_dict)

my_dict.update({"hobby":"playing"})  # update function in Dictionary
print(my_dict)

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items()) # to print key and value pairs

#iteration 
for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)


for key,value in my_dict.items():
    print(key,value)