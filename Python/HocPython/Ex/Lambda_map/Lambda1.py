coordinate2D = [(6,8,4),(2,-1,0),(10,2,7),(-5,9,20)]
print(sorted(coordinate2D))


print(sorted(coordinate2D, key = lambda x : x[2]))
#print(sorted(coordinate2D, key = lambda x : abs(x))

#map(func, seq) , transform each element with the function
list_keyword = ['anh','yeu','em','rat','nhieu'] 
print(list(map(lambda x: x.capitalize(),list_keyword)))

#filter(func, seq) , return all elements with func eqvalute to True
list_number = [1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x: x%2!=0,list_number)))

#reducce(func, seq) , repeatedly applies the func to the elements and return single value.
#func takes 2 arguments
from functools import reduce
seq = [1,3,5,7,9,2,4,6,8]
print(reduce(lambda a,b: a+b, seq))
print(reduce(lambda a,b: a if a>b else b , seq))