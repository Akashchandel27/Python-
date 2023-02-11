#Example:-1 writing data in the files

file=open("C:\Desktop\myfile.txt",'w')
file.write("this is my file statement")
file.close()
print("program completed")

#Example:-2 reading data in the files

file=open("C:\Desktop\myfile.txt",'r')
print(file.read())
print(file.readline())

file.close()

#Example:-3 Appending data into text files

file=open("C:\Desktop\myfile.txt",'a')
file.write("this is my file statement")
file.close()


#over the files

#nsakfna
