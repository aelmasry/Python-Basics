file_name = "my_tasks.txt"
#with open(file_name,'w') as f ---- this automatically closes the file:
f=open(file_name,'a+')
f.write("newlline 1\n")
f.write("New line 2\n")
f.write("new line 3\n")
f.close()
f=open(file_name,'r')
f.seek(3,0)
print(f.read())
print("File written successfully :)")
