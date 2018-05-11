# This code is about how to write to a file:
#there are many ways:
#To replace the existing lines in the File
#to append the lines in the file


# Write to a file: Rewrite the existing lines

text = "Writing to a file"
#Create a file if there is none or use the existing file.
#The file can be of any format
saveFile = open("sample.txt", "w") # "w" - to write to a file
saveFile.write(text) # write the text into the file
saveFile.close() # close the file

# Appending to a file: Append the new lines

text = "appending to a file"
#Create a file if there is none or use the existing file - here we use the existing file.
#The file can be of any format
saveFile = open("sample.txt", "a") # "a" - to append to a file
#It literally places the new entry next to its previous entry to avoid this we can write a new line in between:
saveFile.write('\n')  
saveFile.write(text) # write the text into the file
saveFile.close() # close the file
