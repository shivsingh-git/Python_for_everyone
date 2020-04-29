s=input("Enter The Camel String: ")
l=''
l=s[0]
for i in range(1,len(s)):
    if (s[i].isupper()==True) :
        print(l)
        l=''
        l=s[i]
    else:
        l=l+s[i]
print(l)
    
