#A loop is a programming structure thta can repeat a section of code
#A loop can run the same code exactly over and over, or with some thought, it can generate a pattern
#
#There are two broad categories of loops
#
#Conditional Loops: These loop loop as long as a condition is true
#Counted loops: these loop using a counter to keep track of how many times the loop has run
#
#You can use a loop in any situation, but usually from a design persoective there is a better loop in terms of coding
#
#If you know in adavnce how many times a loop should run, a counted loop is usually a better choice
#If you don't know how many times a loop should run, then a conditional loop is usually the better choice



print("****************************************************************************")
#Taking inputs

word = ""

#A while loop evaluates a condition when it is first reached
#If the condition is true, it enters the loops block
while (len(word) <6 or word.isalpha() == False):
	#Loop block
	word = input("Please input a word larger than 5 letters: ")
	#print(word.isalpha())
	if  (len(word) <6 ):
		print ("Noooooo, I said FIVE")

	if (word.isalpha() == False):
		print("This is likely more than one word or contains characters")
	#When we reach the bottom of the loop block, we check the condition again
	#If it is true, we go back to the top and run it again
print(word+" is a seriously long word!")