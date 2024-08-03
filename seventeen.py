#functions
x=10
def my_function():
    global x
    print(x)
    x=20
    print(x)
my_function()

#arguments
def family_function(fname):
    print(fname + " Surve")
family_function("Suryakant")
family_function("Kinjal")
family_function("Varsha")
family_function("Riya")

#passing 2 arguments
def el_function(fname,lname):
    print(fname + " " + lname)
el_function("Suryakant","Surve")
el_function("Varsha","Surve")

#when passing value is unknown
def add(*num):
    print(num)
add(1,2,3,4) #here 4  
add(100,200) #can add any number of times as here 2..as arguments are unknown


#You can also send arguments with the key = value syntax.
#This way the order of the arguments does not matter...KEYWORD ARGUMENTS
def children(child1,child2,child3):
    print(child1,child2,child3)
children(child3="Tanvi",child1="Riya",child2="Kinjal")

#if we dont call a function by argument it will return by default
def country(names=("INDIA","RUSSIA","SWEDEN")):

    print(names)
country("INDIA")
country("RUSSIA")
country()

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def fruits(names):
    for x in names:
        print(x)
names =["banana","cherry"]   
fruits(names)     


    