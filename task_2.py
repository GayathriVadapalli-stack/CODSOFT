#Simple Calculator
def calculator(a,b,operation):           #defining calculator function
    if operation=='+':                   #Addition
        print(f"{a}+{b} is {a+b}")
    elif operation=='-':                 #Subtraction
        print(f"{a}-{b} is {a-b}")
    elif operation=='*':                 #Multiplication
        print(f"{a}*{b} is {a*b}")       
    elif operation =='/':                #Division
        if b!=0:
            print(f"{a}/{b} is {a/b}")
        else:
            print("Error: Divisible by zero is not defined!")
    else:
        print("Enter a valid operation only from the above options")
print("Welcome to the Calculator")
num_1=float(input("Enter first number: "))     #Taking input from the user 
num_2=float(input("Enter second number: "))
print("Choose the operation you want: \n1.Addition (+)\n2.Subtraction (-) \n3.Multiplication(*)\n4.Division(/)")
operation=input("Enter the operationz(symbol) you want to perform: ")
calculator(num_1,num_2,operation)            #calling calculator function by passing arguments    
print("Thank You")   
