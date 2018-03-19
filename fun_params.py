def print_msg(msg,error="No Error",*args,**kwargs):
    print("Log :"+error," : "+msg)
    print("Kwargs=",kwargs)
    print("Args",args)

print_msg("This will be logged","File Not found",1,-13,0,key_1="abc",key_2="1,3,4")

