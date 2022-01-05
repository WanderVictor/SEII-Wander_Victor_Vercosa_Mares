#File Objects

##Reading Files:
with open("test.txt", "r") as f:
	pass

	##Small Files:
	#f_contents = f.read()
	#print(f_contents)

	##Big Files:
	f_contents = f.readlines()
	print(f_contents)

	###Printing by characters:
	#f_contents = f.read(100)
	#print(f_contents, end = '')
	#f_contents = f.read(100)
	#print(f_contents, end = '')
	#f_contents = f.read(100)
	#print(f_contents, end = '')

	
    
#print(f.mode)
#print(f.closed)
#print(f.read())

###Writing Starts:
#with open("test2.txt", "w") as f:
	#pass
	#f.write("Test")
	#f.seek(0)
	#f.write("Test")
	#f.seek("R")

##Copying Files:
#with open("test.txt", "r") as rf:
	#with open("test_copy.txt", "w") as wf:
		#for line in rf:
			#wf.write(line)