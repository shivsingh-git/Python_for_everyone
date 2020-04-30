#Developers write function and variable names in Camel Case . You are given a string, S, written in Camel Case.
#FindAllTheWordsContainedInIt.
#Sample input: IAmACompetitiveProgrammer
#Sample output: I
#Am
#A
#Competitive
#Programmer
s=input("Enter The Camel String: ")                         #taking the String as a Input
l=''                
l=s[0]                                                      #assigning the frst letter of the string to list l
for i in range(1,len(s)):
    if (s[i].isupper()==True) :                             #if the parser incounters the capital letter 
        print(l)                                            #then print the list
        l=''                                                #making the list empty again
        l=s[i]                                              #assigning the capital letter to the new string
    else:
        l=l+s[i]                                            #assinging all the lower case strings to the list
print(l)                                                    #to print the last string after the last capital letter according to my program
