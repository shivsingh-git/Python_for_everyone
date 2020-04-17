x=input("Enter keywords")
print("The lenght of the keyword is:",len(x))
sum = 0
for i in range(0,101,2):
 sum = sum +i

print("The sum of even numbers in between 1 to 100",sum)

a = [1,2,3,4] 

result = map(lambda x: x*x, a) 
print("The square of the numbes provided is",list(result))
