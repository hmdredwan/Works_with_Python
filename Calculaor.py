#Add Operation
def add_numbers(a,b):
    sum= a+b
    print(f"{a}+{b}={sum}")

#Subtract Operation
def subtract_numbers(a,b):
    sub = a-b
    print(f"{a}-{b}={sub}")

# Multiplication Operation
def multiply_numbers(a,b):
    mul = a*b
    print(f"{a}*{b}={mul}")

# Division Operation
def divide_numbers(a,b):
    div = a/b
    print(f"{a}/{b}={div}")

# Modulus Operation
def mod_number(a,b):
    mod = a%b
    print(f"{a}%{b}={mod}")

print("""Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Modulus""")
print()
while True:
    try:
        choice=input("Enter choice(1/2/3/4/5): ")
        choice=int(choice)
   # try:
        if choice==1 or choice==2 or choice==3 or choice==4 or choice==5:
            print()
            num1 = input("Enter First Number: ")
            num1 = float(num1)
            num2 = input("Enter Second Number: ")
            num2 = float(num2)


            match choice:
                case 1:
                    add_numbers(num1, num2)
                case 2:
                    subtract_numbers(num1, num2)
                case 3:
                    multiply_numbers(num1, num2)
                case 4:
                    #try:
                        divide_numbers(num1, num2)
                    #except Exception as e:
                       # print(e)
                case 5:
                    mod_number(num1, num2)

        else:
            print("Sorry! Your choice are Invalid. Please choice the correct one")
            print()

    except Exception as e:
        print (e)
        print()

    #If user want to perform more calculation
    re_calculate=input("Do you want to calculate more? (yes/no): ").lower()
    if re_calculate!= "yes":
        print ("Good Bye! ")
        print()
        break

