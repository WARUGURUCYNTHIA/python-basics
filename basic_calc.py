def add(num1,num2):
    result=num1+num2
    return result

def sub(num1,num2):
    result=num1-num2
    return result

def div(num1,num2):
    result=num1/num2
    return result

def mult(num1,num2):
    result=num1*num2
    return  result

num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
op = input("Enter the operator: ")

if op=="+":
    print(f"sum is {add(num1,num2)}")
elif op=="-":
    print(f"difference is {sub(num1,num2)}")
    
elif op=="/":
    print("quotient is "+str(div(num1,num2))+".")
    
elif op=="*":
    print(f"the product is {mult(num1,num2)}")
    
else :
    print("Invalid option")    