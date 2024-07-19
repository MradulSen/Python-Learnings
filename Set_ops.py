dict_1= {}  #empty dictionary

set_1 = set() #empty set

set_of_cars = {"audi","volvo","bmw","kia"}
another_set_of_cars = {"maruti","tata","mahindra","kia"}

print(set_of_cars)

set_of_cars.add("skoda")

print(set_of_cars)

set_of_cars.remove("audi")
print(set_of_cars)

union_car = set_of_cars.union(another_set_of_cars)
print(union_car)


intersection_car = set_of_cars.intersection(another_set_of_cars)
print(intersection_car)

print(set_of_cars.difference(another_set_of_cars))

#superset, #subset
a={1,2,3,4,5}
b={2,5}

print(b.difference(a)) 

print(b.issubset(a))