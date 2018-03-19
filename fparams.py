def print_msg(msg,error="No Error",**kwargs):
    print("Log "+error+" : "+msg)
    print(kwargs)

print_msg("This will be Logged","File Not found",key_1="1,2,3")

