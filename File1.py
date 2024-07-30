import os
os.system('cls' if os.name == 'nt' else 'clear') # first 2 lines are to clear screen of terminal before running a code
import pandas
import numpy

'''a= int(input("Enter your first number:"))
b= int(input("Enter your second number:"))
print(int(a) + int(b))
print("The value of", a, "+", b, "is:", a+b)
print("The value of", a, "-", b, "is:", a-b)
print("The value of", a, "*", b, "is:", a*b)
print("The value of", a, "/", b, "is:", a/b)
print("The value of", a, "**", b, "is:", a**b)
print("The value of", a, "//", b, "is:", a//b)
print("The value of", a, "%", b, "is:", a%b)
 print(type(a), type(b))'''


# apple = '''My name is Apple
# I go to Angel School
# My school is in Anand'''
# print(apple)
# banana = "Apply said that I am high in \"Calories\""
# print(banana)
# cacao = 'why is apple arguing with "banana"'
# print(cacao)


'''name = "Dharmik"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[0:3]) #doesnt include the 3rd character
print(name[:3])  #python automatically puts 0 as the beginning index
print(len(name))
print(name[0:-3]) #python interprets it as print(name[0:len(name)-3]) 
print(name[-3:-1]) #print(name[len(name)-3:len(name)-1])  =  print(name(7-3:7-1))  =  print(name[4:6]
for i in name:
    print(i)'''
    

#Strings are immutable
# a = "!!!Harry!! !!!!!!!! Harry"
# print(len(a))  
# print(a)
# print(a.upper())
# print(a.lower())
# print(a.rstrip("!"))
# print(a.replace("Harry", "John"))
# print(a.split(" "))
# blogHeading = "introduction to js"
# print(blogHeading.capitalize())

# str1 = "Welcome to the Console!!!"
# print(len(str1))
# print(str1.center(50))    #centre locates the string in the centre of the total blank string of length provided(50 in this case)
# print(a.count("Harry"))
# str1 = "Welcome to the Console !!!"
# print(str1.endswith("!!!"))    #endswith() checks whethre the string ends with the provided string. It returns a boolean
           
# str1 = "Welcome to the Console !!!"
# print(str1.endswith("to", 4, 10)) #checks whether the string endswith() the provided string within the following indexes

# str1 = "He's name is Dan. He is an honest man."
# print(str1.find("ishh"))
# #print(str1.index("ishh"))    #very similar to find, minor difference (it throws an error if the string is not found)

# str1 = "WelcomeToTheConsole"
# print(str1.isalnum())
# str1 = "Welcome"
# print(str1.isalpha())
# str1 = "hello world"
# print(str1.islower())

# str1 = "We wish you a Merry Christmas\n"
# print(str1.isprintable())

# str1 = "    "  #using Spacebar
# print(str1.isspace())

# str2 = "	"  #using Tab
# print(str2.isspace())

# str1 = "World Health Organization"
# print(str1.istitle())

# str2 = "To kill a Mocking bird"
# print(str2.istitle())

# str1 = "Python is a Interpreted Language"
# print(str1.startswith("Python"))

# str1 = "Python is a Interpreted Language"
# print(str1.swapcase())

# str1="His name is Dan. dan is an honest man."
# print(str1.title())


'''pineapple =input("Enter the price of pineapple: ")
coconut = input("Enter the price of coconut: ")

if(pineapple>coconut):
    print("Pineapple is expensive than coconut")
elif(pineapple == coconut):
    print("Both prices are the same")
else:
    print("Coconut is expensive than  pineepple")'''
    
    
# import time

# timestamp = time.strftime('%H:%M:%S')
# hour = int(time.strftime('%H'))
# print(timestamp)
# if(hour<12):
#     print("Good morning Sir")
# elif(hour>=12):
#     if(hour<16):
#         print("Good Afternoon Sir")
# else:
#         print("good Evening Sir")
    

'''x = 4
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    # Empty case with if-condition
    case _ if x < 10:
        print("x is < 10")
    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _:
        print(x)'''
        
        
        

        
#------------------DAY 17------------------------

'''name = 'Abhishek'
for i in name:
    print(i, end=", ")

colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print(color)
    for i in color:           #Nested for loop
        print(i)
    
    
for k in range(5):
    print(k) 

for k in range(4,9):
    print(k) 
    
for j in range(1,10,2):
    print(j)
''' 



''' WHILE LOOP, BREAK AND CONTINUE
i=int(input("Enter a number: "))
while(i<5):
    print(i)
    i=i+1
else:
    print("Number is bigger than 5")
    
    
do{                    #this is a do-while loop which will always execute once no matter what
    #content
}while(condition);



i = 0
while(i<13):
    
    print("5 X ", i+1, "=", 5*(i+1))
    i = i+1
    if(i==10):
        break          #break terminates the loop
    
    
i=0
for i in range(13):
    if(i==10):
        print("Skip the iteration where i = ", i)
        continue             #continue skips the current iteration(current value of i)
    print("5 X ", i+1, "=", 5*(i+1))



i=0
while True:                 #emulated do-while loop (do while)
    print(i)
    i=i+1
    if(i%100 ==0):                      
        break
    
'''

'''FUNCTIONS

def calculateGeoMean(a,b ):
    mean = (a*b)/(a+b)
    print(mean)

calculateGeoMean(int(input("Enter value of A:")), int(input("Enter value of B:")))



def isGreater(a,b):
    if(a>b):
        print("A is grater")
    else:
        print("B is greater or equal")

isGreater(23,52)




def isLower(a,b):
    pass                              #pass is used when we want to leave a function incomplete, 
                                      #so we can come back and finish it. It doesnt throw and error

'''

'''DAY 21: FUNCTION ARGUMENTS

# def average(a,b,c=1):                     #a and b are compulsary. 
#     print("The average is: ", (a+b+c)/3)


# average(2,b=3)

# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)
# name(mname = "Peter", lname = "Wesker", fname = "Jade")

def average(*numbers):
    sum = 0 
    for i in numbers:
        sum = sum+i 
    # print("The average of the numbers is: ", sum/len(numbers))
    return sum/len(numbers)

c=average(3,4,5,6)
print("The average is :",c)
'''

'''Lists and List Comprehension
#tuple cannot be modified, Lists can be modified


marks = [2,5,7, "Dharmik", True]
print(marks[0])
print(marks[3])
print(type(marks[4]))

if "Dharmik" in marks:
    print("Yes")
else:
    print("No")

lst = [i for i in range(10)]
print(lst)


lst = [i*i for i in range(10)]
print(lst)

lst = [i*i for i in range(10) if i%2==0]
print(lst)

l = [45, 2, 64, 34, 87, 23, 55, 22, 76, 69]
print(l)


l.append(7)
print(l)
l.sort(reverse=True)
print(l)

l.reverse()
print(l)

print(l.index(34))
print(l.count(1))


m = l.copy()      #NEVER use m = l while copying a list in python
m[0] = 0
l.insert(1, 899)     #Inserts the number 899 in the index value 1
print(l)

m = [900, 1000, 1100]
l.extend(m)

k = l + m
print(k)
l.extend(m)
print(l)

'''

'''Day 24 Tuples

#Tuples are immutable. Lists are mutable. Meaning that you cannot change/modify a tuple, 
# but you can modify/update/change a list


tup = (1,)
print(type(tup))

tup2 = (1)
print(type(tup2))

tup3 = (1,4,65,23,"Dharmik", True)

if 65 in tup3:
    print("Yes it is there")
else:
    print("No, its not there")

tup4 = tup3[1:4]
print(tup4)
'''

'''#Day 25 To modify tuples, we have to convert it to a list


tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
# res = tuple1.count(3)

# res = tuple1.index(3)
# res = tuple1.index(311)
# res = tuple1.index(3, 4, 8)
# print(res)
res = len(tuple1)

print('Count of 3 in tuple1 is:', res)
'''

'''Day 28, f-String
letter = "My name is {} and I am from {}"
name="Dharmik"
country="India"
# print(letter.format(name, country))

print(f"My name is {name} and I am from {country}")
print(f"This is how we use f-strings {{name}}, using double curly brackets")

price = 49.903040
txt = f"For only {price:.2f} dollars!"
print(txt)

print(f"{2*30}")         #data type will be string only
'''

'''Day 29 DocString and PEP-8'''

# def square(n):
#     '''Takes a number n, and 
        # returns the square of the number n''' #this is a docstring, it always is written above the function definition
#     print(n**2)
# square(5)
# print(square.__doc__)       #this will print the docstring in the output

''' Day 30 Recursion: function called inside itself 

# def factorial(n):                        #used a normal function 
#     i=n                                     
#     fac = 1
#     if(n>1):
#         for j in range(n):
#             if(i>1):
#                 fac = fac*i
#                 # print(fac, i)
#             else: 
                
#                 # print("Value of fac:",fac)
#                 return fac
#             i = i-1
#     else:
#         fac=1
#         return fac
    
# ans = factorial(int(input("Enter the number :")))
# print("Value of fac is ", ans)

def recFactorial(n):                 #used a recursion function
    if(n==0 or n==1):
        return 1
    else:
        return n * recFactorial(n-1)

print(recFactorial(7))

#fibonacci = 0,1,1,2,3,5,8,13,21,24
def fibonacci(n):
    sum = 0
    if(n==2 or n==1):
        return 1
    elif(n==0):
        return 0
    else:
        return fibonacci(n-1)+fibonacci(n-2)
       
print(fibonacci(5))

'''

'''Day 31 Sets: Order inside sets doesnt matter, it jumbles always
Day 32 Set functions

# s= {2,3,5,6,2}
# print(s)

# info = {"Carla", 19, False, "Dharmik", 4.5, 2, 19}
# print(info)

# harry = set()      #empty set
# #if harry = {}       then this is a dictionary, not a set

# for value in info:
#     print(value)



# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.union(cities2)       
# print(cities3) #doesnt update cities

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.update(cities2)       #updates cities
# print(cities)     


# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.intersection(cities2)     #doesnt update cities
# print(cities3)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.intersection_update(cities2)  #updates cities
# print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.symmetric_difference(cities2)
# print(cities3)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.symmetric_difference_update(cities2)
# print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul", "Delhi"}
# cities3 = cities.difference(cities2)
# print(cities3)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul", "Delhi"}
# print(cities.difference(cities2))


#https://replit.com/@codewithharry/32-Day32-Set-Methods#.tutorial/01%20joining%20sets.md
#too much to copy paste about set functions - Day 32

isdisjoint()    #checks whether 2 sets are completely different
issuperset()
issubset()
add()
update()
remove()/discard()
pop()


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities                          #deletes a set
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()                       #clears/empties a set
print(cities)


info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")
    

'''

'''Day 33 Dictionaries



'''




















































































































































