
x=int(input("Enter the number N"))
list1=[]
print("Enter the loaction index")
for i in range(0,x):
    n=int(input())
    list1.append(n)
print("Now enter the items in list2")    
list2=[]
for i in range(0,x):
    n=input()
    list2.append(n)
list3 = list2

zipped_list = zip(list1,list2)
sorted_pairs = sorted(zipped_list)
tuples = zip(*sorted_pairs)
list1, list2 = [ list(tuple) for tuple in  tuples]
#print(list1)
#print(list2)

for i in range (len(list2)):
    if(list2[i] == list3[i]):
        continue
    elif (len(list2[i]) == i+1):
        list2[i] = list2[i].upper()
    else :
        list2[i] = list2[i].lower()

print(list2)