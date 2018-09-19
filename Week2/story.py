# let the user know what's going on
print ("Welcome to MadLibs!")
print ("Answer the questions below to play.")
print ("-----------------------------------")

# variables containing all of your story info
superhero = raw_input("Who is your favorite super hero?: ")
famousPerson = raw_input("A famous person you dislike: ")
number = raw_input("enter a number between 1-100: ")
animal = raw_input("the cutest animal you can think of: ")
location = raw_input("name a remote location: ")

# this is the story. it is made up of strings and variables.
# the \ at the end of each line let's the computer know our string is a long one
# (a whole paragraph!) and we want to continue more code on the next line. 
# play close attention to the syntax!

story = " Today, " + superhero + " must attempt to save New York City from the dangerous plans that " + famousPerson + "" \
" has made to release " + number + " million of the world's scariest species of " + animal + "" \
" into the streets of Manhattan. The only way to escape might require everyone relocating to " + location+ "" \
" and staying there until the " + animal + " problem has been taken care of by " + superhero + "." 

# finally we print the story
print (story)
