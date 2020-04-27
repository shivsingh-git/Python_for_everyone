def calculator(a,b,operator):
    if operator == 'add' or 'addition':
        return(a+b)
    elif operator == 'subtract' or 'sub':
        return(a-b)
    elif operator == 'multiply' or 'mul':
        return(a*b)
    elif operator == 'devide' or 'devision' or 'dev':
        return(a/b)
    elif operator == 'modulo' or 'mod' or 'remainder':
        return(a%b)
    else :
        print("Error!.. choose your word wisely")    

x,y=int(input().split)
opr=input()
print(calculator(x,y,opr))
