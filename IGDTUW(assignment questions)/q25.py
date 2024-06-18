# Write a program that copies the contents of one text file to another
with open('text.txt','r') as firstfile, open('text1.txt','a') as secondfile: 
	for line in firstfile:  
			secondfile.write(line)
