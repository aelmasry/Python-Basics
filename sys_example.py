import sys
import os
import pdb
#pdb.set_trace() #for debugging
if len(sys.argv) ==  1:
    print("Error. Not sufficient arguments\n Usage: \n 1. To append to a file : python3 sys_example.py -a \"string to add\" \n 2. To display the file: python3 sys_example.py -v")
    sys.exit(1)

if len(sys.argv) >= 1:
    file_name = "task.txt"
    option = sys.argv[1]
    try:
	#append the text to the file task.txt
        if option == '-a':
            if not os.path.isfile(file_name):
                with open(file_name,'w') as f:
                    f.write(sys.argv[2]+"\n")
            else:
                with open(file_name,'a') as f:
                    f.write(sys.argv[2]+"\n")
            print("Added to the file\n")

	#display the contents of the file
        elif option == '-v':
            if not file_name:
                print("Nothing to display!")
                sys.exit(1)
            else:
                with open(file_name,'r') as f:
                    print(f.read())
            print("File END!!")
	
	#delete the contents of the file
        elif option == '-d':
            pass

        else:
            print("invalid arguments")

    except Exception as e:
        print("Error")
    #file_name = sys.argv[1]
    #if not os.path.isfile(file_name):
    #    with open(file_name,'w') as f:
    #        f.write("Written file")
        
