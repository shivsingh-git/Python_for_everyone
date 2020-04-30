#Take as input S, a string. Write a function that replaces every odd character with the character having just higher ascii code and
#every even character with the character having just lower ascii code. Print the value returned.
#Sample input: abcg
#Sample output: badf

s=input("Enter the String")
l=""                                            #creating the new list
j=0                                             #initializing the new variable
x=len(s)
for i in range(1,x+1):                          #runnig the loop from 1 to len to get the position
    if((i%2)==0):                               #checking if the position is odd or not
        l+=(chr(ord(s[j])-1))                   #frst convrting the char to asci,then adding 1 and finally converting it to chr 
        j+=1                                    #incrementing the value of j
    elif((i%2)!=0):
        l+=(chr(ord(s[j])+1))
        j+=1
print(l)                                        #printing the list
