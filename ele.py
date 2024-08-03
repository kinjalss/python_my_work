#THIS FILE CONSISTS OF ALL THE DATATYPES IGNORE THE FUNCTION CREATED


x = "preety"
y = "awesome"

def myfunc():
    global x  # Declare x as global to modify the global variable x
    print(x + " is a compliment") 
    x = "aquarium"  # Modify the global variable x
    print("my fav place is " + x)

myfunc()

def riya():
    global y
    print("riya is " +y)

riya()  
#append and extend...also is mutable can modify list
my_list = [1, 2, 3]
my_list.extend([4,5,6]) #to add many elements in list
print(my_list) 

list = [1,2,3,4]
list.remove(4) #to remove element from list
print(list)

list = [1,2,3,4]
list.append(4) #for adding  an element in python use append as there is no add() method in python
print(list)

#tuple ..is immutable
my_tuple = (1,2,3)
#tuple.append(4)..attribut error as it is immutable
print(my_tuple)

listsec = ["apple", "orange", "cherry"]
listsec.extend(["banana"])  # Correct way to extend a list
print(listsec) #adding string in list
...#.like set list does not have attribute as add instead it has extend,remove

your_list = [1,2,3,4]
your_list[0]=4  #settling 4 at 0 index..supports index as ordered list
print(your_list)
#to add element in list we never use add instead use extend ,appand pr indexposition
#list and tuple both are ordered

#dict..remember the syntax of dict and set are same
my_dict = {"Name":"Kinjal","age":18,"Div": "A"}
print(my_dict)
print(type(my_dict))
 
#set..mutable and unordered
my_set = {"pizza","burger","fries"}
my_set.add("peri peri fries")
my_set.remove("fries")
#my_set[0]="omlette"...do not support indexing as they are unordered collection of elements
print(my_set)


#immutable and unordered
my_frozenset = frozenset({"chickoo", "guava", "sandwich"})  # Creating a frozenset
print(my_frozenset)  # Output: frozenset({'chickoo', 'guava', 'sandwich'})
#my_frozenset[0]="cherry"..cant support coz unordered and immutable
# Attempting to add an element 
#my_frozenset.add("mangoes")
#frozenset can be used in dict as follows
your_dict = {my_frozenset:"Fruits"}
print(your_dict)

#bool
x=True
print(x)
print(type(x))

#range
y=range(6)
print(y)
print(type(y))