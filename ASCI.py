#Take as input S, a string. Write a function that replaces every odd character with the character having just higher ascii code and
#every even character with the character having just lower ascii code. Print the value returned.
#Sample input: abcg
#Sample output: badf
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
