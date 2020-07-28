"""1.  Create a function to open a text file.   
Read the file line by line, inserting each word into a list.  Every sentence in the file should be a list.  You should return a list of lists that contains every sentence in the text file.

2.  Create a function that writes to a text file.
Create a function that takes the name of a text file and a list of lists as a parameter, and creates a textfile with each inner list as a sentence in the text file.
print
"""

def open_file(filename):
  f = open(filename, "r") #r is one of the modes
  sample = f.readlines()
  #we want a list of LISTS (LISTS in this case, are our sentences)
  list1 = []
  #or loop>>> for each line in the sample file
  for line in sample:
    sentences = line.split()
    list1.append(sentences)
  return list1  
   

list2 =  [["Tam", "Nguyen"], ["Kanaya" , "Coleman"] , ["Kayla", "Lemessy"]]

#function for writing an text file
#nf is new file
def write_file(filename, data):
  nf = open("new_file.txt", "w")
  for sentence in data:
    for word in sentence:
      nf.write(word + " ")
    nf.write("\n")
  nf.close()


#TESTING THE FUNCTIONS

#calling the function open_file
print(open_file("sample.txt"))

#calling the function write_file
write_file("newSampleFile", list2)