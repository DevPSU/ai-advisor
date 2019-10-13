#this program grabs all the data from a text file, and line by line classifies it as a class title, or a class description.
#if it is a class title, It is inserted as a key in a dictionary,  If it is a description, it is added as a value to that
#class.

with open("Mined_data.txt", "r") as data:
	all = data.readlines()                         #create a list with each line of the data
	classes = {}                                   #initialize empty dict
	current = ""                                   #this var will hold current class
	currentdesc = ""                               #this var holds current desc of class


	for line in all:                               #iterated through all data
		
		start = line[0:10]                         #grab first 10 chars for efficiency
		                                           #if its a course, it will have 'COURSE ABREVIATION ###:' 
		                                           #so check to see if there is a ':' and a number before it
		pos = start.find(":")-1   				   #grab this char before the ':' 
		if (pos < 0):                              #no ':' means it must be a description, store as val to the key of the current class
			if currentdesc != "":                  #check if its empty, this should only happen first iteration
				currentdesc = classes[current]     #set it to the current desc of the current class
			currentdesc += line					   #add the current line to the desc
			classes.update({current:currentdesc})  #update the current class
			line = data.readline()				   #go to the next line
		else:
			#this is the case where there is a ':' in the line but it still could be a description
			#to check, convert the char before the ':' (remember format is ABREVIATION ###:)
			#to an int, it should work if its a class title.
			try:
				int(line[pos])                     #if the char before the ':' isnt a number, it will throw an exception
			except ValueError:                     #its not a number, so its a description, add it to the class and go to next line
				currentdesc = classes[current]
				currentdesc += line
				classes.update({current:currentdesc})
				line = data.readline()
			else:
				current = line                     #its a class title, so add it to the keys and update the current class
				classes.update({current:""})       #add class to dictionary
				line = data.readline()
for x, y in classes.items():
	print(x, y)									   #print that shit

