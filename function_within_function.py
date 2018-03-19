def hello1():
    def hello2():
        print("Hello world 2")
    print("Hello world 1")
    hello2()

hello1()
hello2() #Throws error
