<<<<<<< HEAD
x=("There are %d types of people.")%10
binary=("binary")
do_not=("don't")
y=("Those who know %s and those who %s.")%(binary, do_not)
print(x)
print(y)
print("I said '%r'."%x)
print("I also said: '%s'."%y)
hilarious= False
joke_evaluation=("Isn't that joke so funny?! %r")
print (joke_evaluation%hilarious)
W='This is the left side of...'
E='a sting with a right side.'
print(W+E)
=======
x= print("There are %d types of people.")%10 #format value not contained within print statement
binary=print("binary") #print statements have no return, so don't assign them to things
do_not=("don't") #parenthesis not needed
y=("Those who know %s and who know %s.")%(binary, do_not)
print(x) #you can't print a print statement
print(y)

print("I said r%.")%(x) #format value not contained within print statement
print("I also said:'%s'.")%(y) #format value not contained within print statement

hilarious= False #false is a reserved word. use a string instead
joke_evaluation=("Isn't that joke so funny?! %r") 
print (joke_evaluation%hilarious #statement missing closing parenthesis
w ="This is the left side of..."
e ="a sting with a right side."
print(w+e)
>>>>>>> 0fa67bd1704bc14401b4b7902335fc9b41e1d70b
