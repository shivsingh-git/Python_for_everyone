#Write a program to print a list of strings in the predefined order, with the following modifications:
#If the string’s length is equal to its printed position, convert string to UPPERCASE
	#- Else convert the string to lowercase
	#- Except if the string’s position is unchanged from its original position
	#- Input will be a number N, then a list of N non-repeating numbers defining the required position of the string, and finally the list of N non-repeating strings. Output will be a list of N strings at the required location, with the required changes.

#- Input:
#5
#5
#4
#3
#1
#2
#Dog
#Goat
#Cat
#Horse
#Elephant

#- Output:
#horse
#elephant
#Cat
#GOAT
#dog

x=int(input("Enter the number N"))
list1=[]
print("Enter the loaction index")
for i in range(0,x):                  #taking input in the string for the indexes.
    n=int(input())
    list1.append(n)
print("Now enter the items in list2")    
list2=[]
for i in range(0,x):                   #taking input in the next string for the names
    n=input()
    list2.append(n)
list3 = list2
zipped_list = zip(list1,list2)         #making a tuple from the two given lists
sorted_pairs = sorted(zipped_list)     #sorting those tuples
tuples = zip(*sorted_pairs)
list1, list2 = [ list(tuple) for tuple in  tuples]    #separating the two lists after sorting
#print(list1)
#print(list2)

for i in range (len(list2)):
    if(list2[i] == list3[i]):                    #checking if the position is same from the original list(cond-3)
        continue
    elif (len(list2[i]) == i+1):                #if the length of the string is equal to the position
        list2[i] = list2[i].upper()
    else :
        list2[i] = list2[i].lower()             #any other case from these two

print(list2)
