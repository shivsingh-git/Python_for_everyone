def calculator(a,b,operator):
    if operator == 'add':
        return(a+b)
    elif operator == 'subtract':
        return(a-b)
    else :
        print("Error choose your word wisely")    

x=int(input())
y=int(input())
s=input()
print(calculator(x,y,s))