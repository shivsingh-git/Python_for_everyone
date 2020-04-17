l=['a','B','c','D']

def CASE(s):
    if(s.isupper()==True):
        s=s.lower()

    else:
       s=s.upper() 
    return s      

x=map(CASE,l) 
print(list(x))      