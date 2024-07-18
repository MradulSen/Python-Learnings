list_of_fruits = [1,2,3,4,"mradul",True,False]

print (type(list_of_fruits))
print (list_of_fruits)

list_of_names = list()
print (type(list_of_names))

"""
which is faster [] or list()

"""

"""
Operations in list
"""

list_of_players = []
list_of_players.append("Virat")
list_of_players.append("Rohit")
list_of_players.append("Jadega")

print(list_of_players)

list_of_players.clear()
print(list_of_players)

list_of_num = [1,1,2,3,4,5,6,6,7,7,7,8,9,10,10,1,1]
list_of_num_new = [12,13,14,15]
print(list_of_num.count(6))  # count of number in the list


list_of_num.extend(list_of_num_new)
print(list_of_num)

print(dir(list_of_num))

