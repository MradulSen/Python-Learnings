t=(1,2,3,4)

##t[2] = 300 #tuple are immutable , values cannot be assigned


print(t[2])

t2=([1,2,3,4],2,3)

t2[0].append(2)  # list inside a tuple can be amended
print(t2)


t2= (20,30,40) #unpacking
print(t2)

a,b,c = (20,30,40) #unpacking
print(a,b,c)


print(t[0:2]) # slicing