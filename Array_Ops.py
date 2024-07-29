import array

arr = array.array('i',[1,2,3])

print(arr)

print(arr[0:2])

arr.append(10)

print(arr)

arr.pop(2)

print(arr)


for i in range (0,2):
    arr.pop()
    print(arr)