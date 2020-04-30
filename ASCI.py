s=input("Enter the String")
l=""
j=0
x=len(s)
for i in range(1,x+1):
    if((i%2)==0):
        l+=(chr(ord(s[j])-1))
        j+=1
    elif((i%2)!=0):
        l+=(chr(ord(s[j])+1))
        j+=1
print(l)       