#Developers write function and variable names in Camel Case . You are given a string, S, written in Camel Case.
#FindAllTheWordsContainedInIt.
#Sample input: IAmACompetitiveProgrammer
#Sample output: I
#Am
#A
#Competitive
#Programmer
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