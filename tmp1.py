# print("Hello world")
a = {"key1":"as",
     "key2":"as2",
     "key3":{"subkey3":"val","subkey4":"val12","subkey5":{'skey':'sfds'}}}
# print(a)

key_var=''
value_var=''
def recfunc(arg):
    global key_var
    global value_var
    for key,val in arg.items():
        if type(val) == dict :
            recfunc(val)
        else: 
            # if n_key:
                # key_var+=n_key+"__"    
            key_var+=key+"__"
            value_var+=val+"__"
print(a)
print(recfunc(a),n_key=None)
print(key_var)
print(value_var)
